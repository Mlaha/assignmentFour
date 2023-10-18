#  grading system ABCD
# no negative values
# no values greater than 100

# 0-30 :D
# 31-50:C
# 51-70:B
# 71-100:A

# MATHS,CHEMISTRY,BIOLOGY,PHYSICS
# the program to display 'unrecognized marks /avg' if a negative value or value greater than  100 is keyed in

def is_valid_mark(mark):
    return 0 <= mark <= 100


def get_grade(average):
    if not is_valid_mark(average):
        return "Unrecognized marks / avg"
    elif average <= 30:
        return "D"
    elif average <= 50:
        return "C"
    elif average <= 70:
        return "B"
    elif average <= 100:
        return "A"

marks = []

subjects = ["Mathematics", "Chemistry", "Biology", "Physics"]

for subject in subjects:
    mark = float(input(f"Enter the marks for {subject}: "))
    if not is_valid_mark(mark):
        print("Unrecognized marks / avg")
        break
    marks.append(mark)

else:
    average = sum(marks) / len(marks)
    grade = get_grade(average)
    print(f"The average grade is: {grade}")