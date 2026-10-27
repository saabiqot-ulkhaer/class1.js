//const -for values that doesnt change
/*const username = "saabiqoh";
const birthday = "2007";
const fruits =["apple", "banana", "orange"];*/ //array
/*const birthYear = 2007;
const currentYear = new Date().getFullYear();
const ge = currentYear - birthYear;

console.log(ge);
*/
//let - for values that can change
/*let age = 2026 - birthday;

console.log(age); // Output: 17 for printing
const use ={
    name: "saabiqoh",//string
    age:18,
    city: "karachi"
} //for objects
console.log(use.name); // Output: saabiqoh for printing name from object
console.log(use.age);
//functions
function greet(name ){
    return "Hello, " + name + "!";
}
console.log(greet("saabiqoh")); // Output: Hello, saabiqoh!
//Arrow function
const add = (a, b) => a + b;
console.log(add(5, 3)); // Output: 8
const isvalid = (email) ==>{
    return email.includes('@') && emails.includes('.')
};
const calculateTotal + (items) ==> {
    return items.reduce((sum, items) ==> sum + (item.price * items.quantity), 0);
};
*/

const  number =[1, 2, 3, 4, 5];
const squaredNumbers = number.map(num => num * 2);
console.log(squaredNumbers); // Output: [2, 4, 6, 8, 10]
const evenNumbers = number.filter(num => num % 2 === 0);
console.log(evenNumbers); // Output: [2, 4]
const foundNumber = number.find(num => num > 3);
console.log(foundNumber); // Output: 4
const sum = number.reduce((acc, num) => acc + num, 0);
console.log(sum); // Output: 15
console.log(`Half of 100 is ${100 / 2}`); // Output: Half of 100 is 50
console.log(typeof 4.5)
let score =65;
let result = score >= 65 ? "Pass" : "Fail"; 
console.log(result); // Output: Pass
/* let theNumber=Number(prompt("Pick a number"));
if(!Number.isNaN(theNumber)){
    console.log("Your number is the square root of " + theNumber * theNumber);
// }*/
// for (let number =0; number <=12; number  =number+2 ){
//     console.log(number);
// }
// let result =1;
// for(let counter=0; counter <10; counter =counter+1 ){
//     result=result*2;
// }
// console.log(result);

let total = 0, count = 1;
while (count <= 10) {
  total += count;
  count += 1;
}
console.log(total);
for(let line = "#"; line.length < 8; line += "#") {
  console.log(line);
}
for(let age=5; age>=3; age--){
    console.log("age is" +age);
}
for(let number=1; number<=100; number++){
    console.log(number);
}