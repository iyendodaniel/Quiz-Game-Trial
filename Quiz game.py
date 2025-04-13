print("Welcome to my computer Quiz!")
points = 0
while True:
    choice = input("Do you wanna play a game ? (yes/no): ").strip().lower()
    if choice == "yes":
        print(f"You chose: {choice}")
        print("Okay! lets play:)")
        print("""Answer the following questions
You have one attempt for each question
For each Question you attempt corrrctly, You get 10 points..... """)
        answer = input("1. How many colors are in Nigeria flag ? ")
        if int(answer) == 2:
         print("You are correct!")
         points += 10
        else:
         print(f"That's not the answer, 2 is the correct answer :)")
        answer = input("2. How many seconds are in 60 minutes? ")
        if int(answer) == 3600:
          print("You are correct!")
          points += 10  
        else:
          print(f"That's not the answer, 3600 is the correct answer :)")
        answer = input("3. What is the fastest land animal in the world ? ")
        if answer.lower() == "cheetah":
         print("You are correct!")
         points += 10
        else:
         print(f"That's not the answer, cheetah is the correct answer :)")

        answer = input("4.What does PC stand for ? ")
        if answer.lower() == "personal computer":
         print("You are correct!")
         points += 10
        else:
         print(f"That's not the answer, personal computer is the correct answer :)")
        answer = input("5. Full meaning of PNG ? ")
        if answer.lower() == "portable network graphic":
         print("You are correct!")
         points += 10
        else:
         print(f"That's not the answer, portable network graphic is the correct answer :)")
         print("You have come to the end of the game....")
        while True:
          choice = input("Would you like to see your total points?  (yes/no): ").strip().lower()
          if choice == "yes":
             print(f"Your Total points: {points} ")
             if points <= 30:
              print("You did well, VERY GOOD")
             else:
              print("You did an Excellent Job")
             break
          elif choice == "no":
           print("Thank you :)")
           quit()
          else:
           print("Please input a valid option (yes or no).")
        break
    elif choice == "no":
        quit()
    else:
         print("Please input a valid option (yes or no).")
