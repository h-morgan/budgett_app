# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 20:19:42 2018

@author: haley
"""
# Enter your salary
salary = int(input("Enter your yearly salary (no commas): "))

# Assume a tax rate of 30%
tax_rate = 0.30

# Calculate your salary after taxes
salary_after_tax = salary * (1 - tax_rate)
print("Salary after taxes: " + str(round(salary_after_tax)))

# Calculate your monthly salary after taxes
monthly_takehome_salary = salary_after_tax / 12
print("Monthly takehome salary: " + str(round(monthly_takehome_salary, 2)))
 
# Input monthly expenses
ask_car_payment = str(input("Do you have a car payment? "))
if ask_car_payment == "yes":
    car_payment = int(input("Enter your monthly car payment: "))
else: 
    car_payment = 0

ask_phone_payment = str(input("Do you have a cell phone payment? "))
if ask_phone_payment == "yes":
    phone_payment = int(input("Enter your monthly cell phone payment: "))
else:
    phone_payment = 0

ask_rent_payment = str(input("Do you have a monthly rent? "))
if ask_rent_payment == "yes":
    rent_payment = int(input("Enter your monthly rent payment: "))  
else:
    rent_payment = 0

ask_credit_card_payment = str(input("Do you have a monthly credit card payment? "))
if ask_credit_card_payment == "yes":
    creditcard_payment = int(input("Enter your monthly credit card payment: "))
else:
    creditcard_payment = 0

ask_public_student_loans = str(input("Do you have any government student loan payments? "))
if ask_public_student_loans == "yes":
    government_loans = int(input("Enter your monthly government student loan payment: "))
else:
    government_loans = 0

ask_private_student_loans = str(input("Do you have any private student loans? "))
if ask_private_student_loans == "yes":
    private_student_loans = int(input("Enter your monthly private student loan payment: "))
else:
    private_student_loans = 0

ask_other_expenses = str(input("Do you have any other monthly expenses? "))
if ask_other_expenses == "yes":
    other_expenses = int(input("Enter the total amount of any other monthly expenses: "))
else:
    other_expenses = 0

# Calculate monthly expenses
monthly_expenses = car_payment + phone_payment + rent_payment + creditcard_payment + government_loans + private_student_loans + other_expenses
print("Your total monthly expenses are $" + str(monthly_expenses))

# Calculate amount remaining after monthly expenses
amount_remaining = monthly_takehome_salary - monthly_expenses
print("Your total amount each month after expenses is: $" + str(round(amount_remaining, 2)))

ask_savings = int(input("How much money would you like to save each month? Enter amount: "))
amount_after_savings = amount_remaining - ask_savings
print("If you plan to save $" + str(ask_savings) + " each month, you will have $" + str(round(amount_after_savings, 2)) + " leftover each month.")




