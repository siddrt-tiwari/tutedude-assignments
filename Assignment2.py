# a = int(input("Enter a number: "))
#
# if a >= 90:
#     print("A")
# elif a >= 80 and a <= 89:
#     print("B")
# elif a >= 70 and a <= 79:
#     print("C")
# elif a >= 60 and a <= 69:
#     print("D")
# elif a < 60:
#     print("F")
# else:
#     print("Invalid value")
#*********************************************************************

# students = {}
#
# while True:
#     print("\n1. Add student")
#     print("2. Update student grade")
#     print("3. Print all students")
#     print("4. Exit")
#
#     choice = input("Enter your choice: ")
#
#     if choice == "1":
#         name = input("Enter student name: ")
#         grade = input("Enter grade: ")
#         students[name] = grade
#         print(f"{name} added successfully.")
#
#     elif choice == "2":
#         name = input("Enter student name to update: ")
#         if name in students:
#             grade = input("Enter new grade: ")
#             students[name] = grade
#             print(f"{name}'s grade updated.")
#         else:
#             print("Student not found.")
#
#     elif choice == "3":
#         if students:
#             print("\nStudent Grades:")
#             for name, grade in students.items():
#                 print(f"{name}: {grade}")
#         else:
#             print("No students found.")
#
#     elif choice == "4":
#         print("Exiting program.")
#         break
#
#     else:
#         print("Invalid choice. Try again.")

#*********************************************************************

# with open("sample.txt", "w") as file:
#     file.write("Hello, this is my first file.\n")
#     file.write("Writing multiple lines in a file.\n")
#
# print("File created and content written successfully.")

#*********************************************************************

# Read from a file
with open("sample.txt", "r") as file:
    content = file.read()

print("File content:")
print(content)