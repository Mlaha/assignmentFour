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

# Function to get the grade based on the average marks
def get_grade(average):
    if average < 0 or average > 100:
        return "Unrecognized marks / avg"
    elif 0 <= average <= 30:
        return "D"
    elif 31 <= average <= 50:
        return "C"
    elif 51 <= average <= 70:
        return "B"
    elif 71 <= average <= 100:
        return "A"

# Input marks for four subjects
maths = float(input("Enter the marks for Mathematics: "))
chemistry = float(input("Enter the marks for Chemistry: "))
biology = float(input("Enter the marks for Biology: "))
physics = float(input("Enter the marks for Physics: "))

# Check if all marks are valid
if is_valid_mark(maths) and is_valid_mark(chemistry) and is_valid_mark(biology) and is_valid_mark(physics):
    # Calculate the average
    average = (maths + chemistry + biology + physics) / 4

    # Get the grade based on the average
    grade = get_grade(average)

    # Print the grade
    print(f"The average grade is: {grade}")
else:
    print("Unrecognized marks / avg")
