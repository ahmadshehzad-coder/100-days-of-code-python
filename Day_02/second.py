# welcome to day two of python progrms

# todayas lesson about primitive datatypes in python


# The datatypes are the.
# 01 .string 
# 02 .integer 
# 03 .float 
# 04 .boolean 

# Examples of Python Data Types

name = "Ahmad Shehzad"     # String
age = 20                   # Integer
price = 99.99              # Float
is_student = True          # Boolean

print(name, type(name))
print(age, type(age))
print(price, type(price))
print(is_student, type(is_student))




# And the second tasks is how to change the datatypes and how to check 

# Original values
num_str = "100"   # string
num_int = 20      # integer
num_float = 45.6  # float
flag = 0          # boolean (0 means False)

# Conversions
print(int(num_str), type(int(num_str)))     # string → int
print(float(num_int), type(float(num_int))) # int → float
print(str(num_float), type(str(num_float))) # float → string
print(bool(flag), type(bool(flag)))         # int → bool





# And also in the next lecture about mathemathical opreations like + - * / // 

# Python Mathematical Operations

a = 10
b = 3

# Addition
print("Addition:", a + b)        # 13

# Subtraction
print("Subtraction:", a - b)     # 7

# Multiplication
print("Multiplication:", a * b)  # 30

# Division
print("Division:", a / b)        # 3.3333333333333335

# Floor Division
print("Floor Division:", a // b) # 3

# Modulus (Remainder)
print("Modulus:", a % b)         # 1

# Exponentiation (Power)
print("Exponent:", a ** b)       # 27

# Combined Operation
print("Combined:", (a + b) * 2 // b)  # 8


# And the next topic about number manipulation




# And the next tasks is tip calcultaor 


# Tip Calculator

# Input: bill amount and tip percentage
bill = float(input("Enter the total bill amount: "))
tip_percent = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

# Calculate tip
tip_amount = bill * tip_percent / 100

# Calculate total bill
total_bill = bill + tip_amount

# Output
print("\nBill Amount:", bill)
print("Tip Amount:", tip_amount)
print("Total Bill to Pay:", total_bill)
