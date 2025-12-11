# Grade Program
# Created by: Shem
# Created on: 2025/12/09
# This program calculates the middle percentage for a given level
# Copyright 2025 Shem
def calc_mark(level):
    # Default return value
    grade = -1
    if level == "4++":
        grade == 95
    elif level == "4+":
        grade = 90
    elif level == "4":
        grade = 85
    elif level == "4-":
        grade = 80
    elif level == "3+":
        grade = 79
    elif level == "3":
        grade = 75
    elif level == "3-":
        grade = 70
    elif level == "2+":
        grade = 69
    elif level == "2":
        grade = 65
    elif level == "2-":
        grade = 60
    elif level == "1+":
        grade = 58
    elif level == "1":
        grade = 55
    elif level == "1-":
        grade = 50
    # invalid input stays as -1
    return grade

def main():
    level = input("Enter the level (1-, 2, 3+, 4++): ")
    mark = calc_mark(level)
    if mark == -1:
        print("Invalid level entered.")
    else:
        print("The middle percentage for " + level + " is " + str(mark) + "%.")


if __name__ == "__main__":
    main()
