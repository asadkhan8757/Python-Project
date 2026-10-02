#Student Grade Calculator

name = input("Enter Student Name:")

maths = float(input("Enter Maths marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))
java = float(input("Enter Java marks: "))
dbms = float(input("Enter Dbms marks: "))

total = maths + english + python + java + dbms
percentage = total / 5

print("\n--- Student Result ---")
print("Name :", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")
