# 💰 Tip Calculator (Python)

A simple **Python console-based Tip Calculator** that helps split a bill fairly among people, including a customizable tip percentage.

---

## 📌 Features

- Takes total bill amount as input
- Allows user to choose tip percentage (10%, 12%, 15%, etc.)
- Splits the final bill equally among multiple people
- Rounds the result to **2 decimal places**
- Beginner-friendly and easy to understand

---

## 🛠️ Technologies Used

- **Language:** Python 3
- **Concepts Used:**
  - User input (`input()`)
  - Type casting (`float`, `int`)
  - Arithmetic operations
  - Rounding (`round()`)
  - f-strings

---

## 🚀 How the Program Works

1. User enters the **total bill amount**.
2. User selects the **tip percentage**.
3. User enters the **number of people** sharing the bill.
4. The program:
   - Calculates the total bill including tip
   - Divides it equally among all people
   - Displays how much **each person should pay**

---

## ▶️ How to Run the Program

```bash
python tip_calculator.py
Make sure you have Python 3 installed.

📷 Sample Output
text
Copy code
Welcome to the tip calculator.
What was the total bill? $150
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 3
Each person should pay $56.0
🧠 Formula Used
text
Copy code
Total Bill with Tip = Total Bill × (1 + Tip / 100)
Amount per Person = Total Bill with Tip ÷ Number of People
🌱 Possible Improvements
Validate inputs (avoid zero or negative numbers)

Add currency formatting (₹ / $ / €)

Allow decimal tip percentages

Add a GUI using Tkinter

Loop to calculate multiple bills

👨‍💻 Author
Mohit
Learning Python step-by-step 🚀
Building logic through small, powerful programs.

