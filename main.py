LEGAL_CHARS = "0123456789"
def isnumeric(text:str) -> bool:
    "returns if ``text`` is a float or integer. Negative values will be not taken into account, there will be False"
    
    if not text: return False
    
    if text.isdecimal(): return True
    
    if text.count('.') == 1:
        
        a,b = text.split('.')
        
        adec, bdec = a.isdecimal() or not a, b.isdecimal() or not b # checks for -> a.b <- 

        #If both a & b False means there something else we dont want... something like letters😨
        if not a and not b: 
            return False
        
        return adec and bdec #both true means it is a floating point value
    
    return False

def get_student_info():
    user_input = input("Enter student name:\n>>> ")
    while not user_input or user_input.isspace() or len(user_input) < 2:
        print(f"Input invalid!")
        user_input = input("Enter student name:\n>>> ")

    english_grade = get_grade('english')
    math_grade = get_grade('math')
    return {'name': user_input, 'english': english_grade, 'math': math_grade}

def get_grade(subject: str) -> float:
    user_input = input(f"Enter grade for [{subject}]:\n>>> ")
    while not isnumeric(user_input):
        print(f"Input invalid!")
        user_input = input(f"Enter grade for [{subject}]:\n>>> ")
    return float(user_input)

def print_student_info(students: list[dict]):
    print(f"{'Best':<15}{'english':<8}{'math':<5}{'avg':<4}best")
    for student in students:
        avg = (student['english'] + student['math']) / 2
        best = max([student['english'] , student['math']])
        print(f"{student['name']:<15}{student['english']:<8}{student['math']:<5}{int(avg):<4}{best}")

def main(debug: bool = False):
    if not debug:
        all_students = []
        for i in range(3): #i assume we have 3 students...
            all_students.append(get_student_info())
    else:
        all_students = [
            {'name':'olivia','english':1,'math': 3},
            {'name':'justus','english':4,'math': 1},
            {'name':'kevin','english':4,'math': 6}
            ]
    print_student_info(all_students)
    

if __name__ == "__main__":
    main(True)