# 💸 GooglePay Expense Sharing

A simple Python program to track shared expenses among friends and calculate who owes whom — inspired by Google Pay's split expense feature.

---

## 👥 Friends in This Project

| Name  | Role             |
|-------|------------------|
| Alice | Paid for hotel   |
| Bob   | Paid for dinner  |
| Carol | Paid for travel  |

---

## 📋 Features

- Add expenses with a payer and list of beneficiaries
- Automatically splits amount equally among beneficiaries
- Calculates net balance for each person
- Displays a clean settlement table using PrettyTable
- Suggests minimum transactions to settle all debts

---

## 🛠️ Dependencies

| Library       | Purpose                        | Install Command           |
|---------------|--------------------------------|---------------------------|
| `numpy`       | Matrix math for expense splits | `pip install numpy`       |
| `prettytable` | Display results as a table     | `pip install prettytable` |

---

## ⚙️ Setup & Installation — Step by Step

### ✅ Step 1 — Check Python is Installed
Open your terminal or command prompt and type:
```
python --version
```
You need **Python 3.7 or above**. If not installed, download from https://www.python.org/downloads/

---

### ✅ Step 2 — Download or Clone This Project

**Option A — Download ZIP:**
1. Go to the GitHub repository page
2. Click the green **"Code"** button
3. Click **"Download ZIP"**
4. Extract the ZIP folder on your computer

**Option B — Clone using Git:**
```
git clone https://github.com/your-username/googlepay-expense-sharing.git
```
Then go into the project folder:
```
cd googlepay-expense-sharing
```

---

### ✅ Step 3 — Install Dependencies

Install both libraries using pip:
```
pip install numpy prettytable
```
Or use the requirements file directly:
```
pip install -r requirements.txt
```

---

### ✅ Step 4 — Run the Program

**In Terminal / Command Prompt:**
```
python expense_sharing.py
```

**In Jupyter Notebook or Google Colab:**
1. Open https://colab.research.google.com
2. Create a new notebook
3. In Cell 1, type and run:
```
!pip install numpy prettytable
```
4. In Cell 2, paste the full code from expense_sharing.py and run it

---

### ✅ Step 5 — View the Output

After running, you will see:

```
Final Settlements:
+--------+------------------------+
| Friend |       Settlement       |
+--------+------------------------+
| Alice  | Should Receive Rs387.08|
| Bob    |      Owes Rs462.92     |
| Carol  | Should Receive Rs522.08|
+--------+------------------------+

Suggested Transactions:
Bob should pay Rs387.08 to Alice
Bob should pay Rs75.83 to Carol
```

---

## 🚀 Usage

### How to Add an Expense

```python
add_expense("Alice", ["Alice", "Bob", "Carol"], 1250)
```

| Parameter       | Description                | Example                     |
|-----------------|----------------------------|-----------------------------|
| payer           | Who paid the bill          | "Alice"                     |
| beneficiaries   | List of people who benefit | ["Alice", "Bob", "Carol"]   |
| amount          | Total amount paid          | 1250                        |

### Sample Expenses Used in This Project

```python
add_expense("Alice", ["Alice", "Bob", "Carol"], 1250)  # Alice paid for everyone
add_expense("Bob",   ["Bob", "Carol"], 800)             # Bob paid for Bob and Carol
add_expense("Carol", ["Alice", "Bob", "Carol"], 1785)  # Carol paid for everyone
```

### How to Add More Friends

Simply update the friends list at the top of the file:
```python
friends = ["Alice", "Bob", "Carol", "David"]
```
The matrix will automatically resize to include the new person.

---

## 📁 Project Structure

```
googlepay-expense-sharing/
│
├── expense_sharing.py   <- Main Python program
├── requirements.txt     <- List of dependencies
└── README.md            <- This file
```

---

## 💡 How It Works

1. expense_matrix (numpy 2D array) stores how much each person paid for each other person.
2. add_expense() fills the matrix by splitting the amount equally among beneficiaries.
3. calculate_settlements() computes total paid minus total owed for each person.
4. display_settlements() shows the result in a clean PrettyTable.
5. suggest_payments() matches debtors with creditors to find minimum transactions needed.

---


## 📌 Notes

- All amounts are in Indian Rupees
- Works in Terminal, VS Code, Jupyter Notebook, and Google Colab
- No database needed — pure Python logic with numpy

---

## 👨‍💻 Author

Created as a Python expense-sharing project inspired by Google Pay split payments.
