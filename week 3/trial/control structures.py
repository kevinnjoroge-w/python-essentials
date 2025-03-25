marks = input("Enter student's marks: ")

try:
    marks = float(marks)
    if marks >= 90:
        print("The student has been awarded an A.")
    elif marks >= 80:
        print("The student has been awarded a B.")
    elif marks >= 70:
        print("The student has been awarded a C.")
    elif marks >= 60:
        print("The student has been awarded a D.")
    else:
        print("The student has failed.The student is advised to retake the unit.")
except ValueError:
    print("Please enter a valid number for the marks.")
