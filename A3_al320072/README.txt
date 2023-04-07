Code by Alex MacLean (AlexM@dal.ca), reused from Assignment 1 and Assignment 2

TODO:
    Fix footer
    Fix second grid in projects.html

Resources used:
    "Build Your Own THEME SELECTOR with JavaScript & CSS" (https://www.youtube.com/watch?v=FEfs0OkjZ9c)
    "Change Style Sheet Using Javascript Tutorial CSS Swap Stylesheet" (https://www.youtube.com/watch?v=_XAQH41rjio)
    "Changing Style Sheet javascript" (https://stackoverflow.com/questions/14292997/changing-style-sheet-javascript)
    "How TO - Hero Image" (https://www.w3schools.com/howto/howto_css_hero_image.asp)

Assignment 3: HTML and CSS (CSCI 1170)
This is a improved version of my original website from Assignment 2.

Actual File Structure:
    A3_al320072/
        -AboutMe.html
        -favicon.png
        -index.html
        -legomovie.png
        -lovelycode.png
        -minecraft.png
        -moshi.css
        -MySong.mp3
        -oldschool.css
        -pianovideo.mp4
        -pictureofme.png
        -projects.html
        -README.txt
        -spaghetti.png
        -styles.css
        -TTTTTT_earlygame.png
        -TTTTTT_lategame.png
        -TTTTTT.py
        -twikipedia.png


Assets/References:
    Photos:
        legomovie.png (https://www.imdb.com/title/tt1490017/)
        twikipedia.png (https://soundcloud.com/twikipedia/born-to-pwn-w-midwxst)
        minecraft.png (https://en.wikipedia.org/wiki/Minecraft)
        spaghetti.png (https://www.cookist.com/spaghetti-bolognese/)
        favicon.png (created by me)
        pictureofme.png (created by me)
        TTTTTT_earlygame.png (created by me)
        TTTTTT_lategame.png (created by me)
    Videos:
        pianovideo.mp4 (https://youtu.be/q2PGQBoei2M)
        "EPIC DUEL - SIMMS v CAMERON (LOSER DIES) #shorts" (https://www.youtube.com/embed/FX8xFQy7BAU)
    Audio:
        MySong.mp3 (created by me)
    Other:
        TTTTTT.py (created by me)

Selectors for part 3 (all in styles.css):
    Universal Selector: Line 71
    Multiple Selector: Line 243
    Child Selector: Line 1
    Sibling Selector: Line 111
    Adjacent Sibling Selector: Line 256
    Attribute Selector: Line 275
    Pseudo-element Selector: Line 287

index.html:
    Requires styles.css to function as intended
    1-9 Setting up html and title/favicon and connecting it to my stylesheet (styles.css)
    10-17 Title/subtitle as well as logo in top right of screen
    18-20 Navbar
    21-35 Table with pictureofme.png and also brief description of myself to server as an introduction to the website
    36-46 Footer
    

projects.html:
    Requires styles.css to function as intended
    1-9 Setting up html and title/favicon and connecting it to my stylesheet (styles.css)
    10-17 Title/subtitle as well as logo in top right of screen
    18-20 Navbar
    21-84 Paragraphs as well as images, audio and videos relating to projects I've done in the past. All assets used can be scene in the assets section of README.txt
    85-95 Footer

AboutMe.html:
    Requires styles.css to function as intended
    1-9 Setting up html and title/favicon and connecting it to my stylesheet (styles.css)
    10-17 Title/subtitle as well as logo in top right of screen
    18-20 Navbar
    21-36 Paragraphs about my previous and current academic experience
    37-87 Table containing unordered lists which contain info about the courses I've taken at dalhousie
    88-104 More paragraphs that include information about myself
    105-150 Table containing top 5 lists about different things that I think are interesting
    151-153 Text and pianovideo.mp4
    154-158 Form that asks the user for a fun fact about themselve and also has a submit button (it doesn't actually submit anywhere)
    159-168 Footer

styles.css, moshi.css, oldschool.css:
    1-7 Fixes logo to top right of the screen
    8-10 Changes background color of entire website to a light gray
    11-13 Sets default style for links
    14-29 Brings title/subtitle to center of screen and styles the text
    31-49 Uses flexboxes to create a navbar below the title, it also styles the text.
    50-65 Uses flexboxes to create a footer, uses positioning to fix to the bottom of the screen and styles the text.
    66-74 Styles table and text within it
    75-90 Adds background images to each part of the table
    91-165 Uses grid to create a 2x3 layout of containing, a list and images
    166-219 Uses grid to create a 3x2 layout containing text, audio and a video
    220-242 Styles table on index.html and styles the image and text within it.
    243-269 Styles the text and lists on AboutMe.html
    270-290 Styles the forms at the bottom of AboutMe.html
    293-455 Changes for phone layout
    457-540 Changes for tablet layout
    542-573 Buttons for theme Changes
    575-580 Hero image

script.js: 
    1-13 Defining function to change theme
    16 Changing the theme to the one stored in local storage.
    18-21 Defining variables for the theme buttons
    24 The fun fact button
    27-32 Contact info alert
    35-37 Knowing when to call the functions for change theme
