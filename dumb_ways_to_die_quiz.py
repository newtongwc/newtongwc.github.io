emma = codesters.Sprite("person8")
emma.go_to(0, -125)
emma.say("This is a quiz based off Internet Safety and how to be safe when on the web!")
stage.wait(5)

candy = 0
#my_display = codesters.Display(my_var, x, y)
candy_display = codesters.Display(candy, -200, 150)

#Question 1
choice = emma.ask("Do you think you make smart choices on the internet? Yes or no?")
if choice == "yes":
    emma.say("Great job! You're gonna ace this quiz!")
    candy = candy + 1
candy_display.update(candy)


if choice == "no":
    emma.say("Well we are here to fix that!")
stage.wait(3)




#Question 2
choice = emma.ask("Are you supposed to socialize with strangers on the web?")
if choice == "yes":
    emma.say("Incorrect! If you have ever done that, never do it again. Strangers are people you shouldn't talk to, because they could be very dangerous.")
    stage.wait(4)

if choice == "no":
    emma.say("Correct! You're a genius")
    stage.wait(4)
    candy = candy + 1
candy_display.update(candy)


#Question 3
choice = emma.ask("Do you give out your passwords to your friends?")
if choice == "yes":
    emma.say("Why! You don't know if that friend will tell someone else.  Also, your friend might use it inappropriatly. The more people that know the worst!")
    stage.wait(4)

if choice == "no":
    emma.say("Good job! That's the right thing to do.  And, never ever give out your password to someone.")
    stage.wait(4)
    candy = candy + 1
candy_display.update(candy)


#Question 4
choice = emma.ask("Have you looked up inappropriate videos or pictures on the web")
if choice == "yes":
    emma.say("If you have ever done that, never do it again it is not appropriate")
    stage.wait(4)

if choice == "no":
    emma.say("Good, way to stay safe!")
    stage.wait(2)
    candy = candy + 1
candy_display.update(candy)


#Question 5
choice = emma.ask("Have you bought a purse or something from a website you go to often?")
if choice == "yes":
    emma.say("Correct! If you have ever done that, what did you get! Lucky duck!")
    stage.wait(4)
    candy = candy + 1
candy_display.update(candy)

if choice == "no":
    emma.say("Incorrect! You're a genius")
    stage.wait(2)
candy_display.update(candy)


#Question 6
choice = emma.ask("Do you post pictures of where you go on vacation pubicly?")
if choice == "yes":
    emma.say("Incorrect! If you have ever done that, never do it again. You never know who sees these pictures.  They might even rob your house because they know your not home")
    stage.wait(4)

if choice == "no":
    emma.say("Correct! You're a genius")
    stage.wait(2)
    candy = candy + 1
candy_display.update(candy)


#Question 7
choice = emma.ask("Have you downloaded an app that has access to your personal information?")
if choice == "yes":
    emma.say("Incorrect! If you have ever done that, never do it again. You never know what information they can access.")
    stage.wait(4)


if choice == "no":
    emma.say("Correct! You're a genius")
    stage.wait(2)
    candy = candy + 1
candy_display.update(candy)


#Question 8
choice = emma.ask("Have you opened an email from your soccer coach about a soccer game?")
if choice == "yes":
    emma.say("Correct! You're a genius.")
    stage.wait(2)
    candy = candy + 1
candy_display.update(candy)

if choice == "no":
    emma.say("Incorrect! If you've ever opened up an email from an unknown email address, did you know it could be spam?")
    stage.wait(4)
candy_display.update(candy)


#Question 9
choice = emma.ask("Have you ever seen and clicked on an ad that said win a free ipad with 3 easy instructions?")
if choice == "yes":
    emma.say("Incorrect! If you have ever done that, never do it again. They will ask you for private information and they might even track you!")
    stage.wait(4)

if choice == "no":
    emma.say("Correct! If you see ads like that, stay away from them and don't click on them.")
    stage.wait(4)
    candy = candy + 1
candy_display.update(candy)

emma.say("Well it looks like that's the end! Hope you had a fun time!  You score is" candy " out of nine!") 
stage.wait(9)
emma.ask("This is the link! (https://youtu.be/XcjyM72Agsc)  Feel free to copy and paste to watch an awesome and fun filled video! THANKS A LOT!!:)")



