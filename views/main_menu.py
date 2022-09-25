from .components import menu
from .main_menu_list import subject_menu
from models.subjects_model import init_subjects

def main_menu():
    init_subjects()
    subjects = subject_menu()
    menu("--Main Menu", "What would you like to do? ", subjects, "--INVALID INPUT: Type what you'd like to do")
    