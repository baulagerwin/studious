from pyfiglet import Figlet

from views.components import menu
from views.main_menu_list import subject_menu
from models.subjects_model import init_subjects

def main():
    print(intro())
    print(get_started())
    subjects = subject_menu()
    main_menu("--Main Menu", "What would you like to do? ", subjects, "--INVALID INPUT: Type what you'd like to do")

def intro():
    figlet = Figlet()
    figlet.setFont(font="small")
    first_line = figlet.renderText("Welcome to Studious")
    second_line = "An application where you can review a subject by generating a random question with their respective answer."
    third_line = "\n"
    return first_line + second_line + third_line

def get_started():
    return input("Press enter to continue...")

def main_menu(menu_text, prompt, list_to_map, error_msg):
    init_subjects()
    menu(menu_text, prompt, list_to_map, error_msg)

if __name__ == "__main__":
    main()