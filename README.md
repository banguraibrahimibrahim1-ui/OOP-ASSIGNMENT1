STUDENT RESULTS MANAGEMENT SYSTEM
Course: PROG211 – Object-Oriented Programming (OOP1)
Project Title: Student Results Management System
Programming Language: Python 3
Application Type: Console-Based Application
1. Project Overview
The Student Results Management System is a Python-based application developed to help schools manage students' academic results. The system allows users to register students, record marks for different subjects, calculate total marks and averages, assign grades, and generate individual student result reports.
The application uses Object-Oriented Programming (OOP) principles to organize its code into classes and methods. It also uses a Python dictionary to store student records during program execution.
The main purpose of the project is to reduce manual calculations, improve the organization of academic records, and make the process of managing student results easier and more accurate.
2. Main Features
The system provides the following features:
1.	Student Registration: Allows users to register students using their student ID and full name.
2.	Result Recording: Allows users to enter marks for different subjects.
3.	Automatic Calculation: Calculates students' total marks and average scores.
4.	Grade Assignment: Automatically assigns grades based on students' average marks.
5.	Individual Result Report: Displays the academic performance of a particular student.
6.	Student Summary: Displays all registered students and their average scores.
7.	Class Average: Calculates the overall average of all recorded subject marks.
8.	Input Validation: Prevents invalid marks, duplicate student IDs, and empty student details.
9.	Sample Data: Provides sample student records for testing and demonstration.
3. System Requirements
To run the application, the following requirements are needed:
•	Python 3 installed on the computer.
•	Visual Studio Code, PyCharm, IDLE, or another Python code editor.
•	A computer running Windows, Linux, or macOS.
•	No external Python libraries are required.
4. Installation and Execution
Follow these steps to run the application:
1.	Download the Student_Results_Management_System.py file.
2.	Save the file in a folder on your computer.
3.	Open the folder using Visual Studio Code or another Python editor.
4.	Open the terminal.
5.	Run the following command:
python Student_Results_Management_System.py
If your computer uses the Python 3 command, run:
python3 Student_Results_Management_System.py
6.	The main menu will appear on the screen.
7.	Enter the number corresponding to the operation you want to perform.
5. How to Use the System
When the application starts, the following menu is displayed:
===================================================
          STUDENT RESULTS MANAGEMENT SYSTEM
===================================================

MAIN MENU

1. Register student
2. Record student result
3. View one student's result
4. Display all students
5. Calculate overall class average
6. Load sample data
7. Exit

Choose an option (1-7):
Menu Operations
Option	Description
1	Register a new student
2	Record a student's subject mark
3	View an individual student's result
4	Display all registered students
5	Calculate the overall class average
6	Load sample student records
7	Exit the application
6. Sample Input and Output
The following examples demonstrate how the system works.
Example 1: Registering a Student
Sample Input:
Choose an option (1-7): 1

Enter student ID: ST004
Enter student name: Abdul Sesay
Expected Output:
Student Abdul Sesay registered successfully.
Example 2: Recording Student Results
Sample Input:
Choose an option (1-7): 2

Enter student ID: ST004
Enter subject name: Mathematics
Enter mark (0-100): 85
Expected Output:
Result recorded successfully.
The same process can be repeated to record marks for English and Computer Studies.
Example 3: Viewing an Individual Result
Assuming the following marks have been recorded:
•	Mathematics: 85
•	English: 75
•	Computer Studies: 90
Sample Input:
Choose an option (1-7): 3

Enter student ID: ST004
Expected Output:
================================================
             STUDENT RESULT REPORT
================================================
Student ID : ST004
Name       : Abdul Sesay
------------------------------------------------
Subject                         Mark
------------------------------------------------
Mathematics                    85.00
English                        75.00
Computer Studies               90.00
------------------------------------------------
Total                         250.00
Average                        83.33
Grade                              A
================================================
Example 4: Displaying All Students
Sample Input:
Choose an option (1-7): 4
Expected Output:
===================================================
              STUDENT RESULTS MANAGEMENT SYSTEM
===================================================
Student ID    Student Name               Average     Grade
--------------------------------------------------------------------
ST004         Abdul Sesay                    83.33           A
===================================================
Example 5: Calculating the Overall Class Average
Sample Input:
Choose an option (1-7): 5
Expected Output:
Overall class average: 83.33%
The class average is calculated using all the subject marks recorded for all registered students.
7. Sample Data
The system includes sample records that can be loaded using menu option 6.
Student ID	Student Name	Mathematics	English	Computer Studies
ST001	John Kamara	80	75	85
ST002	Mary Sesay	65	70	60
ST003	Ibrahim Koroma	45	50	40
These records are provided to demonstrate the system's functionality and help users test the different operations.
Note: Loading the sample data more than once during the same program session will produce duplicate student ID errors because the system prevents duplicate registrations.
8. Grading System
The application uses the following example grading scale:
Average Mark	Grade
80–100	A
70–79	B
60–69	C
50–59	D
Below 50	F
The system calculates the average mark and automatically assigns the appropriate grade.
This grading scale is for demonstration purposes and can be adjusted to follow the official grading policy of a particular institution.
9. Object-Oriented Programming Concepts
The application demonstrates the following OOP concepts:
9.1 Classes and Objects
The project contains two main classes:
•	Student: Represents an individual student and stores their personal details and academic results.
•	ResultsManagementSystem: Manages student registration, result recording, calculations, and reports.
Objects are created from these classes to perform the different operations of the system.
9.2 Attributes
Attributes store information belonging to an object. Examples include:
•	student_id
•	name
•	results
•	school_name
•	students
9.3 Instance Methods
Instance methods perform operations using the data stored in an object. Examples include add_result(), calculate_total(), calculate_average(), and register_student().
9.4 Class Method
The system_description() method uses the @classmethod decorator to provide general information about the application.
9.5 Dictionary Data Structure
The application uses a dictionary to store student objects. The student ID serves as the dictionary key, while the corresponding student object serves as the value.
This makes it easier to organize and retrieve student records.
10. Alignment with Digital Public Goods (DPG) Standards
Digital Public Goods (DPGs) are digital solutions that can support sustainable development and provide benefits to the public. They are generally expected to promote openness, accessibility, privacy, security, interoperability, and responsible technology use.
The Student Results Management System demonstrates several principles associated with Digital Public Goods.
10.1 Open Source and Transparency
The application is developed using Python, an open-source programming language. Its source code can be inspected, studied, modified, and improved by developers.
This supports transparency and encourages collaboration because other developers and educational institutions can understand how the application works and adapt it to their needs.
10.2 Accessibility and Inclusion
The system uses a simple text-based interface that can run on computers with basic hardware. It does not require expensive software licenses or advanced computer equipment.
This can make the solution more accessible to schools and educational institutions with limited technological resources.
10.3 Data Privacy and Protection
Student academic records are important information and should be handled responsibly. The application keeps records in memory during program execution and does not transmit them to an external server.
This reduces unnecessary external data sharing. However, the current version does not include user authentication, encryption, or permanent secure storage. These features should be introduced before the system is used to manage real student records.
10.4 Reusability and Adaptability
The application is organized into separate classes and methods. Other developers can reuse or modify these components when developing similar educational applications.
For example, the system can be expanded to support attendance management, school fees, student profiles, and academic reporting.
10.5 Interoperability
The application uses Python data structures and clearly organized source code. Its design can be extended to connect with databases and other educational management systems.
At present, it does not provide an API or direct integration with external systems. These capabilities can be introduced in future versions.
10.6 Contribution to Sustainable Development
The system supports Sustainable Development Goal 4 (Quality Education) by providing a digital approach to managing academic performance and student results.
It can help educational institutions improve record organization and reduce the time spent on manual result calculations.
10.7 Responsible Use and Limitations
The application is a small educational prototype. Although it demonstrates principles associated with Digital Public Goods, it has not been independently assessed or certified as a Digital Public Good.
Before public or institutional deployment, it would require stronger security, privacy controls, documentation, testing, and additional technical improvements.
11. Limitations of the System
The current version has some limitations:
1.	Student records are stored temporarily in memory.
2.	Records are lost when the application is closed.
3.	There is no login or authentication system.
4.	The application does not connect to a database.
5.	It does not provide a graphical user interface.
6.	It does not generate downloadable or printable result sheets.
12. Future Improvements
The system can be improved by introducing:
•	MySQL or PostgreSQL database integration.
•	User authentication for administrators and teachers.
•	A graphical user interface using Python Tkinter.
•	Editing and deleting student records.
•	Exporting result reports to PDF or Excel.
•	Additional subjects and configurable grading scales.
•	Automatic backup and secure storage of academic records.
13. Project File Structure
The project currently contains the following main file:
Student_Results_Management_System/
│
├── Student_Results_Management_System.py
│
└── README.md
•	Student_Results_Management_System.py contains the main Python application.
•	README.md explains the project, installation, usage, sample input/output, and DPG alignment.
14. Conclusion
The Student Results Management System demonstrates how Python and Object-Oriented Programming can be used to solve a practical problem in the education sector. It provides basic functions for registering students, recording marks, calculating averages, assigning grades, and displaying academic reports.
The project also demonstrates important DPG-related principles such as open-source development, accessibility, reusability, transparency, and responsible data handling. Although the current version is a basic prototype, it provides a foundation for developing a more complete and secure school results management application.
