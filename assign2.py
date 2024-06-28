import numpy as np

def generate_pay_slip():
    # Get number of employees
    num_employees = int(input("Enter the number of employees: "))
    
    # Initialize arrays to store employee information
    employee_numbers = np.empty(num_employees, dtype=int)
    employee_names = np.empty(num_employees, dtype=str)
    departments = np.empty(num_employees, dtype=str)
    basic_pays = np.empty(num_employees, dtype=float)
    
    # Input employee information
    for i in range(num_employees):
        print(f"\nEnter details for Employee {i+1}:")
        employee_numbers[i] = int(input("Enter Employee Number: "))
        employee_names[i] = input("Enter Employee Name: ")
        departments[i] = input("Enter Department: ")
        basic_pays[i] = float(input("Enter Basic Pay: "))

    # Calculate PF, HRA, loan, DA, and total salary for each employee
    pf = 0.08 * basic_pays
    hra = 0.12 * basic_pays
    loan = 0.11 * basic_pays
    da = 0.25 * basic_pays
    total_salaries = basic_pays + da + hra - pf - loan

    # Display pay slips for all employees
    print("\nPay Slips\n")
    for i in range(num_employees):
        print(f"Employee Number: {employee_numbers[i]}")
        print(f"Employee Name: {employee_names[i]}")
        print(f"Department: {departments[i]}")
        print(f"Basic Pay: {basic_pays[i]}")
        print(f"PF (8%): {pf[i]}")
        print(f"HRA (12%): {hra[i]}")
        print(f"Loan (11%): {loan[i]}")
        print(f"DA (25%): {da[i]}")
        print(f"Total Salary: {total_salaries[i]}\n")
"Adding new changes here"

# Main function
if __name__ == "_main_":
    generate_pay_slip()