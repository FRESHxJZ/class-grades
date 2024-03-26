
#Bryon Garcia
#class csc 110 hw 1
#due date 9-7-23

i = 1
total = 0

homework = float(input("Enter Homework grade: "))
total = 40 * (homework/100) 
midterm = float(input("Enter Midterm grade: "))
total = total + (30 * (midterm/100))
finalexam = float(input("Enter Final Exam grade: "))
total = total + (30 * (finalexam/100))
i += 1
total = round(total, 2)

print ("Your final grade is : ", total)
