import datetime
import math
import random
import uuid
import os
import time
import string

import file_operations as fo


# 1. DATETIME OPERATIONS

def datetime_menu():
    while True:
        print("\n--- Datetime and Time Operations ---")
        print("1. Display current date and time")
        print("2. Difference between two dates")
        print("3. Format date")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            print("Current Date and Time:", datetime.datetime.now())

        elif ch == "2":
            try:
                d1 = input("Enter first date (YYYY-MM-DD): ")
                d2 = input("Enter second date (YYYY-MM-DD): ")

                date1 = datetime.date.fromisoformat(d1)
                date2 = datetime.date.fromisoformat(d2)

                print("Difference:", abs((date2 - date1).days), "days")

            except ValueError:
                print("Invalid date format!")

        elif ch == "3":
            now = datetime.datetime.now()
            print(now.strftime("%d-%m-%Y %H:%M:%S"))

        elif ch == "4":
            input("Press Enter to start stopwatch...")
            start = time.time()

            input("Press Enter to stop stopwatch...")
            end = time.time()

            print("Elapsed Time:", round(end - start, 2), "seconds")

        elif ch == "5":
            try:
                seconds = int(input("Enter countdown seconds: "))

                if seconds < 0:
                    print("Enter a non-negative number!")
                    continue

                while seconds > 0:
                    print(seconds)
                    time.sleep(1)
                    seconds -= 1

                print("Time's up!")

            except ValueError:
                print("Please enter an integer!")

        elif ch == "6":
            break

        else:
            print("Invalid choice!")


# 2. MATHEMATICAL OPERATIONS

def math_menu():
    while True:
        print("\n--- Mathematical Operations ---")
        print("1. Calculate Factorial")
        print("2. Calculate Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            try:
                n = int(input("Enter a non-negative integer: "))

                if n < 0:
                    print("Number must be non-negative!")
                else:
                    print("Factorial:", math.factorial(n))

            except ValueError:
                print("Invalid input!")

        elif ch == "2":
            try:
                p = float(input("Enter principal amount: "))
                r = float(input("Enter annual interest rate (%): "))
                t = float(input("Enter time in years: "))

                if p < 0 or r < 0 or t < 0:
                    print("Values must be non-negative!")
                    continue

                amount = p * (1 + r / 100) ** t
                ci = amount - p

                print("Compound Interest:", round(ci, 2))
                print("Total Amount:", round(amount, 2))

            except ValueError:
                print("Invalid input!")

        elif ch == "3":
            try:
                degree = float(input("Enter angle in degrees: "))
                radian = math.radians(degree)

                print("Sin:", round(math.sin(radian), 4))
                print("Cos:", round(math.cos(radian), 4))
                print("Tan:", round(math.tan(radian), 4)
                      if abs(math.cos(radian)) > 1e-10
                      else "Undefined")

            except ValueError:
                print("Invalid angle!")

        elif ch == "4":
            print("\n1. Circle")
            print("2. Rectangle")
            print("3. Triangle")

            shape = input("Choose shape: ")

            try:
                if shape == "1":
                    r = float(input("Enter radius: "))

                    if r < 0:
                        print("Radius cannot be negative!")
                    else:
                        print("Area of Circle:", round(math.pi * r * r, 2))

                elif shape == "2":
                    l = float(input("Enter length: "))
                    w = float(input("Enter width: "))

                    if l < 0 or w < 0:
                        print("Dimensions cannot be negative!")
                    else:
                        print("Area of Rectangle:", l * w)

                elif shape == "3":
                    b = float(input("Enter base: "))
                    h = float(input("Enter height: "))

                    if b < 0 or h < 0:
                        print("Dimensions cannot be negative!")
                    else:
                        print("Area of Triangle:", 0.5 * b * h)

                else:
                    print("Invalid shape!")

            except ValueError:
                print("Invalid input!")

        elif ch == "5":
            break

        else:
            print("Invalid choice!")


# 3. RANDOM DATA GENERATION

def random_menu():
    while True:
        print("\n--- Random Data Generation ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            try:
                a = int(input("Enter minimum value: "))
                b = int(input("Enter maximum value: "))

                if a > b:
                    print("Minimum cannot exceed maximum!")
                else:
                    print("Random Number:", random.randint(a, b))

            except ValueError:
                print("Invalid input!")

        elif ch == "2":
            try:
                n = int(input("Enter list size: "))
                a = int(input("Enter minimum value: "))
                b = int(input("Enter maximum value: "))

                if n < 0 or a > b:
                    print("Invalid values!")
                else:
                    values = [
                        random.randint(a, b) for _ in range(n)
                    ]
                    print("Random List:", values)

            except ValueError:
                print("Invalid input!")

        elif ch == "3":
            try:
                n = int(input("Enter password length: "))

                if n < 1:
                    print("Length must be at least 1!")
                else:
                    characters = string.ascii_letters + string.digits + "!@#$%"
                    password = "".join(
                        random.choices(characters, k=n)
                    )
                    print("Generated Password:", password)

            except ValueError:
                print("Invalid input!")

        elif ch == "4":
            otp = random.randint(100000, 999999)
            print("Generated OTP:", otp)

        elif ch == "5":
            break

        else:
            print("Invalid choice!")


# 4. UUID GENERATION

def uuid_menu():
    print("\n--- Generate Unique Identifier ---")
    print("Generated UUID:", uuid.uuid4())


# 5. CUSTOM FILE OPERATIONS

def file_menu():
    while True:
        print("\n--- File Operations ---")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            fo.create_file()

        elif ch == "2":
            fo.write_file()

        elif ch == "3":
            fo.read_file()

        elif ch == "4":
            fo.append_file()

        elif ch == "5":
            break

        else:
            print("Invalid choice!")


# 6. EXPLORE MODULE ATTRIBUTES

def explore_module():
    module_name = input("Enter module name (math, random, os): ")

    modules = {
        "math": math,
        "random": random,
        "os": os,
        "datetime": datetime,
        "uuid": uuid
    }

    if module_name in modules:
        print("Available Attributes:")
        print(dir(modules[module_name]))
    else:
        print("Module not available in this program!")


# MAIN MENU

def main():
    while True:
        print("\n==============================")
        print(" Welcome to Multi-Utility Toolkit")
        print("==============================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_menu()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()