"""
name: Arika Awan
date: september 26
description: you work at a dog boarding facility. you need to find the
number of small dogs and large dogs boarded, the total revenue for the day,
total expenses for the day, and the profit. user inputs number of large dog boarded
"""

#ask user for how many large dogs are currently boarded
l_dogs = int(input())

#calculate the amount of small dogs
s_dogs = 8-l_dogs

#calculate how much you made boarding large dogs
cost_l_dogs = l_dogs * 25

#calculate how much you made boarding small dogs
cost_s_dogs = s_dogs *20

#calculate total revenue
total_revenue = cost_l_dogs + cost_s_dogs

#calculate expenses
total_expenses = 30 + (2*8)

#calculate profit
profit = total_revenue - total_expenses

#output
print("Number of Small Dogs Currently Boarded:",s_dogs)
print("Number of Large Dogs Currently Boarded:",l_dogs)
print(f"Total Revenue for the Day: ${total_revenue}")
print(f"Total Expenses for the Day: ${total_expenses}")
print(f"Today's Profit: ${profit}")

