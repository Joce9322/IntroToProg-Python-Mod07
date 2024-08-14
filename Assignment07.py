# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   JMunoz,8/12/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# TODO Create a Person Class
class Person:
    """
    A class representing person data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.

    ChangeLog:
        - JMunoz, 8.12.2024: Created the class.
    """

# TODO Add first_name and last_name properties to the constructor (Done)
    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name  = last_name
# TODO Create a getter and setter for the first_name property (Done)
    @property
    def first_name(self):
        return self.__first_name.title()  # formatting code
        '''
        Returns the first_name as a title
        :return: The first name, properly formatted
        Change Log
        -JMunoz, 8.12.2024: Created getter for the first_name property 
        '''
    @first_name.setter
    def first_name(self, value:str):
        '''
        Sets the first name while doing validations
        :param value: The value to set
        :return: None
        '''
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

# TODO Create a getter and setter for the last_name property (Done)
    @property
    def last_name(self):
        '''
        Returns the last_name as a title
        :return: The last name, properly formatted
        Change Log
        -JMunoz, 8.12.2024: Created getter for the last_name property
        '''
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value:str):
        '''
        Sets the last name while doing validations
        :param value: The value to set
        :return: None
        '''
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

# TODO Override the __str__() method to return Person data (Done)
    def __str__(self):
        return f'{self.first_name},{self.last_name}'

# TODO Create a Student class the inherits from the Person class (Done)
class Student(Person):
    """
    A class representing student data.

    Properties:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        gpa (float): The gpa of the student.

    ChangeLog: (Who, When, What)
    JMunoz,8.12.2024,Created Class, added properties and private attributes, and moved
        first_name and last_name into a parent class
    """

# TODO call to the Person constructor and pass it the first_name and last_name data (Done)
# TODO add a assignment to the course_name property using the course_name parameter (Done)
    def __init__(self, first_name:str = '', last_name:str = '', course_name:str = ''):
        super().__init__(first_name=first_name, last_name=last_name)
        self.course_name = course_name

# TODO add the getter for course_name (Done)
    @property
    def course_name(self):
        '''
        Returns the course name
        :return: course name
        '''
        return self.__course_name

# TODO add the setter for course_name (Done)
    @course_name.setter
    def course_name(self, value:str):
        '''
        Sets the course name
        :param value: The value to set
        :return: None
        '''
        self.__course_name = value

# TODO Override the __str__() method to return the Student data (Done)
    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.course_name}'
        #another way to override string is by calling on parent class (person):
        #return f'{super().__str__()}, {self.course_name}'


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    JMunoz,8.3.2024,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads student registration data from a json file

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created Function

        :param file_name: string for the file name
        :param student_data: list of dictionary rows containing student registration content
        :return student_data

        """

        try:
            file = open(file_name, "r")
            list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
            for student in list_of_dictionary_data:  # Convert the list of dictionary rows into Student objects
                student_object: Student = Student(first_name=student["FirstName"],
                                                  last_name=student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_object)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes student registration data to a json file

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created Function

        :param file_name: string for the file name
        :param student_data: list of dictionary rows containing student registration content

        """

        try:
            list_of_dictionary_data: list = []
            # Convert List of Student objects to list of dictionary rows.
            for student in student_data:
                student_json: dict \
                    = {"FirstName": student.first_name,
                       "LastName": student.last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)
            #Read data
            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    JMunoz,8.3.2024,Created Class

    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :param message: string displaying custom error messager
        :param Exception: exception to print
        :return: None

        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :param menu: string displaying the menu message
        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """
        This function outputs the current students registered for courses

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :param student_data: list of dictionary rows containing student registration content
        :return: None

        """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student.first_name} '
                  f'{student.last_name} is enrolled in {student.course_name}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
        JMunoz,8.3.2024,Created function

        :param student_data: list of dictionary rows containing student registration content
        :return: student_data: list of dictionary rows containing student registration content

        """
        try:
            student = Student()
            student.first_name = input("Enter the student's first name: ")
            student.last_name = input("Enter the student's last name: ")
            student.course_name = input("Please enter the name of the course: ")
            student_data.append(student)
            print()
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
