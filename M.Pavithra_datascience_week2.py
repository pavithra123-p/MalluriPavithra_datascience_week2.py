##DATA SCIENCE  ASSIGNMENT 

#Task 1: Basic Operations
#Accepts two integer inputs from the user.
a =int(input("enter a first number:"))
b=int(input("enter a second number: "))

#Performs the following operations using arithmetic operators: 
#Prints the results in a well-formatted way using f-strings. 
# Addition
print(f"addition of (a+b)={a+b}")
#subtraction
print(f"subtraction of (a-b)={a-b}")
# Multiplication
print(f"Multiplication of (a*b)={a*b}")
#Division
print(f"Division of (a/b)={a/b}")
# Modulus
print(f"Modulus of (a%b)={a%b}")
#Exponentiation
print(f"Exponentiation of (a**b)={a**b}")

 # Task 2: Working with Lists and Arrays 

 #Create a list containing at least 10 numbers.
li=[2,5,7,9,23,78,61,45,3,11,27]

#length of the list
print(len(li))

#  printing maximum value in a list
m=max(li)
print(f"maximum value in list is {m}")

# printing minimum value in a list
mn =min(li)
print(f"Minimum value in list is {mn} ")

# Add a new element to the list and remove one element. 
li.append(39)
print(f"39  is added to list {li}")
li.remove(27)
print(f"27 is removed from list {li}")

# sorting the list in asceding and descending order
asc = sorted(li)
print(f"ascending order  {asc}")
desc = sorted(li,reverse =True)
print(f" desecnding order{desc}")

#3. Convert the list into a NumPy array and calculate
import numpy as np
arr = np.array(li)
print(arr)
# mean of numpy array
arr1=np.mean(arr)
print(f"mean of array is{arr1}")
arr2=np.median(arr)
print(f"median of numpy array{arr2}")
arr3=np.std(arr)
print(f"standard deviation of numpy array{arr3}")

#Task 4: File Handling
# Step 1: Create and write data to the text file
with open("student_data.txt", "w") as file:
    file.write("Pavithra,Data Science,89\n")
    file.write("Rahul,Python,72\n")
    file.write("Anjali,AI,95\n")
    file.write("Kiran,ML,66\n")
    file.write("Sneha,Data Analytics,78\n")

print("Data written to student_data.txt")

# Step 2: Read the file and display students with marks > 75
print("\nStudents with marks above 75:")

with open("student_data.txt", "r") as file:
    for line in file:
        name, course, marks = line.strip().split(",")
        marks = int(marks)

        if marks > 75:
            print(f"Name: {name}, Course: {course}, Marks: {marks}")
