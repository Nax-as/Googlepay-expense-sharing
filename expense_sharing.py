!pip install numpy prettytable

import numpy as np
from prettytable import PrettyTable

friends = ["Alice", "Bob", "Carol"]
expense_matrix = np.zeros((len(friends), len(friends)))  # Rows: Who paid, Columns: Who it's for


def add_expense(payer, beneficiaries, amount):
    payer_idx = friends.index(payer)
    share_per_person = amount / len(beneficiaries)
    for beneficiary in beneficiaries:
        beneficiary_idx = friends.index(beneficiary)
        expense_matrix[payer_idx][beneficiary_idx] += share_per_person


def calculate_settlements():
    total_paid = np.sum(expense_matrix, axis=1)   # How much each person paid
    total_owed = np.sum(expense_matrix, axis=0)   # How much each person owes
    net_balance = total_paid - total_owed          # Positive: person should receive, Negative: person owes
    return net_balance


def display_settlements():
    settlements = calculate_settlements()

    table = PrettyTable()
    table.field_names = ["Friend", "Settlement"]

    for i, friend in enumerate(friends):
        if settlements[i] > 0:
            table.add_row([friend, f"Should Receive \u20b9{settlements[i]:.2f}"])
        elif settlements[i] < 0:
            table.add_row([friend, f"Owes \u20b9{-settlements[i]:.2f}"])
        else:
            table.add_row([friend, "Is Settled"])

    print("\nFinal Settlements:")
    print(table)


def suggest_payments():
    settlements = calculate_settlements()

    creditors = [(friends[i], amt) for i, amt in enumerate(settlements) if amt > 0]
    debtors   = [(friends[i], -amt) for i, amt in enumerate(settlements) if amt < 0]

    transactions = []

    # Match debtors to creditors
    while debtors and creditors:
        debtor,   debt_amount   = debtors.pop(0)
        creditor, credit_amount = creditors.pop(0)

        payment = min(debt_amount, credit_amount)
        transactions.append((debtor, creditor, payment))

        # Adjust balances
        debt_amount   -= payment
        credit_amount -= payment

        # Re-add to list if any balance remains
        if debt_amount > 0:
            debtors.insert(0, (debtor, debt_amount))
        if credit_amount > 0:
            creditors.insert(0, (creditor, credit_amount))

    print("\nSuggested Transactions:")
    if transactions:
        for debtor, creditor, amount in transactions:
            print(f"{debtor} should pay \u20b9{amount:.2f} to {creditor}")
    else:
        print("No transactions needed. Everyone is settled.")


# Input expenses
add_expense("Alice", ["Alice", "Bob", "Carol"], 1250)   # Alice paid ₹1250 for Alice, Bob, and Carol
add_expense("Bob",   ["Bob", "Carol"], 800)              # Bob paid ₹800 for Bob and Carol
add_expense("Carol", ["Alice", "Bob", "Carol"], 1785)   # Carol paid ₹1785 for everyone

# Display final settlement
display_settlements()

# Suggest payments to settle debts
suggest_payments()
