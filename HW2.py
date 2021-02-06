# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from the console, the computer makes a decision randomly.

import random


# def game():
#     """Function that simulates the game "rock, scissors, paper"""
#
#     value_list = ["rock", "scissors", "paper"]
#     player_choose = False
#     computer = random.choice(value_list)
#
#     while player_choose == False:
#         player_choose = input("Choose: rock, scissors, paper?")
#         player_choose = player_choose.lower()
#         player_choose = player_choose.strip()
#
#         if player_choose == computer:
#             res = "Dear heat"
#         elif player_choose == "rock":
#             if computer == "scissors":
#                 res = "You win!"
#             else:
#                 res = "You lose! :("
#         elif player_choose == "scissors":
#             if computer == "paper":
#                 res = "You win!"
#             else:
#                 res = "You lose! :("
#         elif player_choose == "paper":
#             if computer == "rock":
#                 res = "You win!"
#             else:
#                 res = "You lose! :("
#         else:
#             res = "Incorrect data entered. Try again!"
#     return res


# 2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days at any given time.
# Do you have enough toilet paper(TP) to make it through?
# Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
# and the average person uses 57 sheets per day.

#
# def tp_estimation(my_dict):
#     """The function of calculating the remains of toilet paper for 14 days for a given number of people"""
#
#     sheets_in_roll = 500
#     sheets_for_person = 57
#     count_days = 14
#     count_rolls = my_dict["tp"]
#     count_persons = my_dict["people"]
#
#     estimation = count_rolls*sheets_in_roll/sheets_for_person/count_persons/count_days
#     if estimation >= count_days:
#         res = "Stocks of toilet paper are sufficient"
#     else:
#         res = "Oh, think you should shop"
#
#     return res
#
#
# res = tp_estimation({"people": 1, "tp": 100})
# print(res)


# Create a function that will receive a dictionary with two key/values:
# "people" ⁠— Number of people in the household.
# "tp" ⁠— Number of rolls.
# Return a statement telling the user if they need to buy more TP!

# 3) Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Example:
# encrypt("banana") ➞ "0n0n0baca"
# encrypt("karaca") ➞ "0c0r0kaca"
# encrypt("burak") ➞ "k0r3baca"
# encrypt("alpaca") ➞ "0c0pl0aca"

# def encrypt(value):
#     """Encryption function with conditions: 1 step -  Reverse, 2 step - Replacing vowels with numbers"""
#
#     value = value[::-1]
#     value = value.replace("a", "0")
#     value = value.replace("e", "1")
#     value = value.replace("i", "2")
#     value = value.replace("o", "2")
#     value = value.replace("u", "3")
#     return value
#
#
# res = encrypt("qaqaqa")
# print(res)


# **4)Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win
# for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
# Example:
# tic_tac_toe([
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]) ➞ "X"
#
# tic_tac_toe([
#     ["O", "O", "O"],
#     ["O", "X", "X"],
#     ["E", "X", "X"]
# ]) ➞ "O"
#
# tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ]) ➞ "Draw"


# def tic_tac_toe(value):
#     """Functions that return the result of the game of tic-tac-toe"""
#
#     a = []
#     for i in value:
#         for ii in i:
#             a.append(ii)
#
#     if a[0] == a[1] == a[2]:  # верхняя горизонталь
#         res = a[0]
#     elif a[3] == a[4] == a[5]:  # средняя горизонталь
#         res = a[3]
#     elif a[6] == a[7] == a[8]:  # нижняя горизонталь
#         res = a[6]
#     elif a[0] == a[3] == a[6]:  # левая вертикаль
#         res = a[0]
#     elif a[1] == a[4] == a[7]:  # средняя вертикаль
#         res = a[1]
#     elif a[2] == a[5] == a[8]:  # правая вертикаль
#         res = a[2]
#     elif a[0] == a[4] == a[8]:  # диагональ сверху вниз
#         res = a[0]
#     elif a[6] == a[4] == a[2]:  # диаголь снизу вверх
#         res = a[6]
#     else:
#         res = "Draw"  # ничья
#
#     return res
#
#
# test = tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ])
#
# print(test)