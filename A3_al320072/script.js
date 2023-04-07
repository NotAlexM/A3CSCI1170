//Defining function to change theme
function changeStyle(newSheet) {
    document.getElementById("pageStyle").setAttribute("href", newSheet);
    if (localStorage.getItem("style") != newSheet){
        if (newSheet == "styles.css"){
            window.confirm("Reverting to Default");
        }
        else{
            window.confirm("Changing Theme!"); 
        }
    }
    localStorage.setItem("style", newSheet);
}
//I learned how to use local storage to store the theme from "Build Your Own THEME SELECTOR with JavaScript & CSS", link in README.txt

changeStyle(localStorage.getItem("style" || "styles.css"))

//Defining Buttons
const defaultThemeButton = document.getElementById('default-button');
const oldschoolThemeButton = document.getElementById('oldschool-button');
const moshiThemeButton = document.getElementById('moshi-button');

//Fun fact button
document.getElementById("sendFun").onclick = function () {document.getElementById("sendFun").setAttribute("value", "Fun Fact Sent!")};


//Contact info alert
if (document.querySelector('ul li ul li:first-child') != null){
    if (document.querySelector('ul li ul li:first-child').textContent == "My Professor was Dr. Siegel"){
        window.confirm("Be sure to check out my contact info at the bottom of the page!");
    }
}

//Knowing when to call the functions (credit to "Changing Style Sheet javascript" for helping me fix errors, link in README.txt)
oldschoolThemeButton.onclick = function () { changeStyle("oldschool.css") };
moshiThemeButton.onclick = function () { changeStyle("moshi.css") };
defaultThemeButton.onclick = function () { changeStyle("styles.css") };

