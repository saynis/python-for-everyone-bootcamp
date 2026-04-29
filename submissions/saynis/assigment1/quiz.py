# Name: Mohamed abdifatah  (Saynis)
# Description: A simple English Quiz program for assignment one
# 1. Greeting
name= input("What is your name? ")
print("welcome ," + name)

#2. Questions
#Q1
score = 0

print("variable is a reserved word in python?")
Ans1= input(" your answer:")
if Ans1 == "True" or Ans1 == "true":
    score += 1
    print(" your are Correct!")
else:
    print("Wrong! The correct answer is True.")

#Q2
print("What is the output of 2 + 3 * 4?")
Ans2= input(" your answer:")
if Ans2 == "14":
    score += 1
    print(" your are Correct!")
else:
    print("Wrong! The correct answer is 14.")  


#Q3
print("Which of the following is a comparison operator in Python?")
print("a) +")
print("b) -")
print("c) ==")
Ans3= input(" your answer:")
if Ans3 == "c" or Ans3 == "C":
    score += 1
    print(" your are Correct!")
else:
    print("Wrong! The correct answer is c) ==")


#3. Final Score
print(name + " , your final score is: " + str(score) + " out of 3.")
