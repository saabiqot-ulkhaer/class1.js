import random
import tkinter as tk

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
PLAYER_SIZE = 40
FALLING_SIZE = 30
INITIAL_SPEED = 5
SPAWN_INTERVAL_MS = 900
UPDATE_INTERVAL_MS = 30


class FallingDodgeGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Falling Dodge")
        self.resizable(False, False)
        self.canvas = tk.Canvas(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="#111111")
        self.canvas.pack()

        self.score_text = self.canvas.create_text(
            10, 10, anchor="nw", fill="#ffffff", font=("Arial", 16, "bold"), text="Score: 0"
        )
        self.message_text = self.canvas.create_text(
            WINDOW_WIDTH / 2,
            WINDOW_HEIGHT / 2,
            fill="#ffffff",
            font=("Arial", 20, "bold"),
            text="Press Enter to Start",
        )

        self.player = None
        self.blocks = []
        self.score = 0
        self.speed = INITIAL_SPEED
        self.running = False
        self.move_direction = 0

        self.bind_all("<KeyPress>", self.on_key_press)
        self.bind_all("<KeyRelease>", self.on_key_release)
        self.reset_game()

    def reset_game(self):
        self.canvas.delete("block")
        if self.player:
            self.canvas.delete(self.player)
        self.blocks = []
        self.score = 0
        self.speed = INITIAL_SPEED
        self.running = False
        self.move_direction = 0
        self.player_x = WINDOW_WIDTH / 2
        self.player_y = WINDOW_HEIGHT - PLAYER_SIZE - 10
        self.player = self.canvas.create_rectangle(
            self.player_x - PLAYER_SIZE / 2,
            self.player_y - PLAYER_SIZE / 2,
            self.player_x + PLAYER_SIZE / 2,
            self.player_y + PLAYER_SIZE / 2,
            fill="#1abc9c",
        )
        self.canvas.itemconfigure(self.score_text, text="Score: 0")
        self.canvas.itemconfigure(self.message_text, text="Press Enter to Start")

    def start_game(self):
        if self.running:
            return
        self.running = True
        self.canvas.itemconfigure(self.message_text, text="")
        self.score = 0
        self.speed = INITIAL_SPEED
        self.blocks.clear()
        self.canvas.after(SPAWN_INTERVAL_MS, self.spawn_block)
        self.update_game()

    def game_over(self):
        self.running = False
        self.canvas.itemconfigure(self.message_text, text=f"Game Over! Score: {self.score}\nPress Enter to Play Again")

    def spawn_block(self):
        if not self.running:
            return
        x = random.randint(FALLING_SIZE // 2, WINDOW_WIDTH - FALLING_SIZE // 2)
        block = self.canvas.create_rectangle(
            x - FALLING_SIZE / 2,
            -FALLING_SIZE,
            x + FALLING_SIZE / 2,
            0,
            fill="#e74c3c",
            tags="block",
        )
        self.blocks.append(block)
        self.speed = INITIAL_SPEED + int(self.score / 15)
        interval = max(300, SPAWN_INTERVAL_MS - self.score * 4)
        self.canvas.after(interval, self.spawn_block)

    def update_game(self):
        if not self.running:
            return

        self.move_player()
        self.move_blocks()
        self.check_collisions()
        self.score += 1
        self.canvas.itemconfigure(self.score_text, text=f"Score: {self.score}")
        self.canvas.after(UPDATE_INTERVAL_MS, self.update_game)

    def move_player(self):
        if self.move_direction == 0:
            return

        self.player_x += self.move_direction * 10
        self.player_x = max(PLAYER_SIZE / 2, min(WINDOW_WIDTH - PLAYER_SIZE / 2, self.player_x))
        self.canvas.coords(
            self.player,
            self.player_x - PLAYER_SIZE / 2,
            self.player_y - PLAYER_SIZE / 2,
            self.player_x + PLAYER_SIZE / 2,
            self.player_y + PLAYER_SIZE / 2,
        )

    def move_blocks(self):
        for block in self.blocks[:]:
            self.canvas.move(block, 0, self.speed)
            x1, y1, x2, y2 = self.canvas.coords(block)
            if y1 > WINDOW_HEIGHT:
                self.blocks.remove(block)
                self.canvas.delete(block)

    def check_collisions(self):
        player_coords = self.canvas.coords(self.player)
        overlapping = self.canvas.find_overlapping(*player_coords)
        for item in overlapping:
            if item in self.blocks:
                self.game_over()
                return

    def on_key_press(self, event):
        key = event.keysym.lower()
        if key in ["left", "a"]:
            self.move_direction = -1
        elif key in ["right", "d"]:
            self.move_direction = 1
        elif key == "return":
            self.start_game()

    def on_key_release(self, event):
        key = event.keysym.lower()
        if key in ["left", "a", "right", "d"]:
            self.move_direction = 0


if __name__ == "__main__":
    game = FallingDodgeGame()
    game.mainloop()
