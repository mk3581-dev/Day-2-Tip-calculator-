print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))

# Calculate total bill including tip
total_with_tip = total_bill * (1 + tip / 100)

# Calculate each person's share
bill_per_person = total_with_tip / total_people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay ${final_amount}")
