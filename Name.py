import keyboard
from Student import Student
from Student import Teacher
while True:
    def minimize(S):
        N = S.replace(" ", "")
        G = N.capitalize()
        return G
    gender = input("Are you a male or a female?")
    Gender = minimize(gender)
    if Gender == ("Female"):
        print("You are a female.")
        break
    elif Gender == ("Male"):
        print("You are a male.")
        break
    elif Gender == ("Gay") or Gender == ("Homosexual"):
        print("Look, I'm not homophobic, but that's not an answer. Try again.")
    else:
        print("That is not a valid gender. Try again.")
while True:
    def minimize(c):
        y = c.replace(" ", "")
        C = y.capitalize()
        return C
    name = input("What is your name?")
    Name = minimize(name)
    answ = input("So your name is " + Name + "?")
    Answ = minimize(answ)
    if Answ == ("Yes"):
        break
    elif Answ == "No":
        print("OK.")
    else:
        print("Answer yes or no.")
MathTeacher = (Teacher, "Ms. Bluezárd", )
story_lines = ["You wake up. It's 6:00 AM. You hate waking up at 6:00 AM.",
"Mom: " + Name + ", you are late for school!",
"It's 6:00 AM and your LATE for school. You hate your life.",
"Mom: " + Name + ", why haven't you come down yet? Come On!",
"You decide to go downstairs.",
"Mom: Son, I've made you Breakfeast.",
"You eat Breakfeast.",
"It tastes good, but still doesn't change the fact that your life sucks.",
"Mom: Now grab your backpack. The school bus is waiting outside.",
"You grab your backpack and enter the school bus.",
"Bus Driver: 'Ello there Mate! pick a seat and we'll be off.",
"You spot a seat in the back next to some disgusting dude.",
"As you walk towards the empty seat you see him sticking booger from his nose on his chair",
"Disgusting Dude: Have you seen the LiveCheat prototype? They say it cheats life!",
"Disgusting Dude: It will change human lifestyle FOREVER!",
"You decide to look for another seat.",
"You find a seat in the front and sit there.",
"You arrive at school. As always, your classmate Tales encounters you.",
"Tales: " + Name + " we're late for class! "+MathTeacher+" is waiting for us!",
MathTeacher+": " + Name + "! Why are you late?"
]
for line in story_lines:
    print(line)
    enter = "p"
    while enter.replace(" ", "") != "":
        enter = input()
        if enter.replace(" ", "") != "":
            print("press enter to proceed.")