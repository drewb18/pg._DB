import pyautogui as pg
import time
import webbrowser

points = 0

# Question
answer = pg.prompt(
"""
What is your greatest achievement?

a) Earning my greenbelt
b) Playing in my band
c) Starting the Dundies

"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
    
# Question
answer = pg.prompt(
"""
What would you rather do?

a) Tend a beet farm
b) Eat M&Ms
c) Create a film called "Treat level Midnight"

"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3
    

# Question
answer = pg.prompt(
"""
What do you do in your free time?

a) Plan to hurt Jim
b) Eat M&Ms
c) "Creative thinking"

"""
    )

# Answer
pg.alert("You chose " + answer)

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


#END OF SURVEY`
pg.alert("You are...")

# Dwight should be a
if points < 5:
    pg.alert("Dwight Schrute!")
    webbrowser.open("https://www.youtube.com/watch?v=jgsPJVZY5pM")
# Kevin should be b
elif points >= 5 and points <8:
    pg.alert("Kevin Mallone!")
    webbrowser.open("https://www.youtube.com/watch?v=w4jI97DiHF8")
# Michael should be c
elif points >= 7:
    pg.alert("Michael Scott!")
    webbrowser.open("https://www.youtube.com/watch?v=ClzJkv3dpY8")
