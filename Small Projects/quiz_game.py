print("Welcome to my Computer Quiz")


playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay! Let's Play!!!")

score = 0

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + "  questions correct")

print("You got " + str((score/4)* 100) + "%")
