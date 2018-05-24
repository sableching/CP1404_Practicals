from prac_07.programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)

    programmes = [ruby, python, visual_basic]

    print("The dynamically typed languages are:")
    for program in programmes:
        if program.is_dynamic():
            print(program.title)


main()