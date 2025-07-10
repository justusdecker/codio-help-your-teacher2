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

def get_student_info() -> dict[str, str | float]:
    """ returns name, *classes as dict """
    user_input = input("Enter student name:\n>>> ")
    while not user_input or user_input.isspace() or len(user_input) < 2:
        print(f"Input invalid!")
        user_input = input("Enter student name:\n>>> ")

    english_grade = get_grade('english')
    math_grade = get_grade('math')
    return {'name': user_input, 'english': english_grade, 'math': math_grade}

def get_grade(subject: str) -> float:
    """ get grade from a student """
    while 1:
        user_input = input(f"Enter grade for [{subject}]:\n>>> ")
        if isnumeric(user_input):
            grade = float(user_input)
            if 0 <= grade <= 100:
                return float(user_input)
            else:
                print('Input invalid! Grade must be between 0 and 100.')
                
def print_student_info(students: list[dict]) -> None:
    """ print the ``name``, ``grades`` of each class, ``average`` grade & ``best`` grade for each student """
    print(f"{'Best':<15}{'english':<8}{'math':<5}{'avg':<6}best")
    for student in students:
        avg = (student['english'] + student['math']) / 2
        best = max([student['english'] , student['math']])
        print(f"{student['name']:<15}{student['english']:<8}{student['math']:<5}{avg:<6}{best}")
        
def check_user_input_until_integer(prompt:str) -> int:
    """
    Continuously prompts the user for input until a valid integer is provided.
    Returns the to int converted user_input
    """
    user_input: str = ""
    while not user_input:
        user_input = input(prompt)
        user_input = user_input if user_input.isdecimal() else ""
    return int(user_input)

def main(debug: bool = False) -> None:
    """ The main logic of the program """
    if not debug:
        all_students = []
        for i in range(check_user_input_until_integer('How many student do you want to add?: ')): #i assume we have 3 students...
            all_students.append(get_student_info())
    else:
        all_students = [
            {'name':'olivia','english':1,'math': 3},
            {'name':'justus','english':4,'math': 1},
            {'name':'kevin','english':40,'math': 100}
            ]
    print_student_info(all_students)
    

if __name__ == "__main__":
    main(False)