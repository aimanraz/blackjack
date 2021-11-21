############### Blackjack Project #####################


import random
import os 
from blackjack_art import logo
clear = lambda: os.system('cls')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card ():
  """ Take a random card from the deck """
  random_card = cards[random.randint(0,len(cards)-1)]
  return random_card

def calculate_score(list_cards):
  """ Take the user cards and calculate the scores """
  scores = sum(list_cards)
  if scores == 21:
    return 0
  elif scores > 21 and 11 in list_cards:
    list_cards[len(list_cards)-1] = 1
    scores = sum(list_cards)
    return scores
  else:
    return scores

def compare(user_score, computer_score):
  """ Compare the comp and user score for judgement """
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for i in range(0,2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}\n")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")

      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()

