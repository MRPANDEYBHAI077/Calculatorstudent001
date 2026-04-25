# Student Grade Calculator
def calculate_grade():
    print("--- BCA Student Grade System ---")
    
    # Input marks
    sub1 = float(input("Enter marks for C Programming: "))
    sub2 = float(input("Enter marks for Web Development: "))
    sub3 = float(input("Enter marks for Mathematics: "))
    
    total = sub1 + sub2 + sub3
    percentage = (total / 300) * 100
    
    # Logic for grading
    if percentage >= 80:
        grade = "A+"
    elif percentage >= 60:
        grade = "A"
    elif percentage >= 40:
        grade = "B"
    else:
        grade = "Fail"
        
    print(f"\nTotal Marks: {total}/300")
    print(f"Percentage: {percentage}%")
    print(f"Final Grade: {grade}")

calculate_grade()

