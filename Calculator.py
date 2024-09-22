""" BASIC CALCULATOR USING PYTHON"""
# Define functions for each arthemetic functions..

def add(a,b):
    #Function to add two numbers.
    return a + b

def subtract(a,b):
    #Function to subtract two numbers.
    return a - b

def multiply(a,b):
    #Function to multiply two numbers.
    return a * b

def divide(a,b):
    #Function to divide two numbers.
    if(b == 0):
        return "Error! division by 0 is not allowed"
    else:
        return a / b

def calculator():
    # Main function for calculator program.

    print("\nBASIC CALCULATOR\n")
    print("Select an operation:")
    print("1. addition")
    print("2. subtraction")
    print("3. multiply")
    print("4. division\n")

    while True:
        choice = input("Enter your choice (1/2/3/4): \n")

        # Taking choice input by user.  
        if choice in ('1','2','3','4'):

            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

            except ValueError:
                print("Invalid input. Please enter numerical values.")

                continue 

            # Perform operations..
            if choice == '1':
                print(f"\nThe result of addition is: {add(num1, num2)}\n")

            elif choice == '2':
                print(f"The result of subtraction is: {subtract(num1, num2)}\n")

            elif choice == '3':
                print(f"The result of multiplication is: {multiply(num1, num2)}\n")

            elif choice == '4':
                print(f"The result of division is: {divide(num1, num2)}\n")
        
        else:
                print("Invalid choice. Please select a valid operation.\n")  

        # Ask user if they want to perform another calculation..

        next_calculation = input("Do you want to perform another calculation? (yes/no):")

        if(next_calculation != 'yes'):
             print("\nThank you for using our calculator.GOODBYE!")  
             break

if __name__ == "__main__":
     calculator()