# ---------------------------------------------------------------------------- #
# Title: Assignment 07 - Pickling and Error Handling
# Dev: Isepp Rebane
# Description: Script using classes, functions, and error handling that takes user task and priority info,
# and places it into a .dat file using pickle.1
#
# CHANGE LOG:
# I, Rebane - 06/03/2023 - Initial Commit
#----------------------------------------------------------------------------#

import pickle

#File variable
file_name_str = "ToDo.dat"

#Main Class-----------------------------------------------------------#
class main:
    """main script class"""

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) name of file:
        :return: (list) contains priority and choice
        """
        try:
            table_lst = []
            objFile = open(file_name, "rb")
            contents = pickle.load(objFile)
            objFile.close()
            print(contents)
        except Exception as error:
            print("There was a non-specific error!")
            print("Built-In Python error info: ")
            print(error.__doc__)
            print(error.__str__())

    @staticmethod
    def write_data_to_file(file_name):
        """ Writes data to a file

        :param file_name: (string) name of file:
        :return (list) file entries:
        """
        try:
            task = str(input("Please Enter Task:"))
            priority = str(input("Please Enter Priority:"))
            table_lst = {"Task": str(task).strip(), "Priority": str(priority).strip()}
            file = open(file_name, "ab")
            pickle.dump(table_lst, file)
            file.close()
            print ("File Saved!")
            print ("Task:", table_lst["Task"], ",", "Priority:", table_lst["Priority"])
        except Exception as error:
            print("There was a non-specific error!")
            print("Built-In Python error info: ")
            print(error.__doc__)
            print(error.__str__())
    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user
        :param: (string) user input
        :return: null
        """
        print('''
        Please Choose Fro The Following:
        
        1) See Current Priority And Due Date
        2) Replace Current Priority And Due Date    
        3) Exit Program
        ''')
        print()

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :param: (string) user menu input
        :return: (string) choice
        """
        choice = str(input("Which option would you like to perform? [1 to 3] - ")).strip()
        print()
        return choice

#Main Body of Script-------------------------------------------------------#

#Display Menu To User
while True:
    #Get User Input
    main.output_menu_tasks()
    choice_str = main.input_menu_choice()

    #Show Current Tasks
    if choice_str.strip() == "1":
        main.read_data_from_file(file_name=file_name_str)

    #Add New Task And Write To File
    elif choice_str.strip() == "2":
        main.write_data_to_file(file_name=file_name_str)

    #Exit Program
    elif choice_str == '3':
        print("Goodbye!")
        break