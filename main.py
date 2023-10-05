
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculate the tip amount
tip_amount = bill * (tip_percentage / 100)

# Calculate the total amount including tip
total_amount = bill + tip_amount

# Calculate the amount each person should pay
pay_per_person = total_amount / people

# Format the result to 2 decimal places
pay_per_person = "{:.2f}".format(pay_per_person)

print(f"Each person should pay: ${pay_per_person}")
