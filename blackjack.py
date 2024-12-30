import random

from replit import clear

from art import logo



def deal_card():

  '''Returns a random card from the deck of cards'''

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  return random.choice(cards)







def calculate_score(cards):

  '''Takes a list of cards and returns the score of cards entered'''

  if len(cards) == 2 and sum(cards) == 21:

    return 0

  if 11 in cards and sum(cards) > 21:

    cards.remove(11)

    cards.append(1)

  return sum(cards)



def compare(user_score,computer_score):

  if user_score > 21 and computer_score > 21:

    return "You went over. You lose"

  if user_score == computer_score:

    return ("It's a draw")

  elif computer_score == 0:

    return ("Computer has blackjack and you lose.")

  elif user_score == 0:

    return ("You have blackjack and computer lose.")

  elif user_score > 21:

    return ("You went over and you lose.")

  elif computer_score > 21:

    return ("Computer went over and you win.")

  elif user_score > computer_score:

    return ("You win!")

  else:

    return ("You lose!")



def game():

  print(logo)

  user_cards = []

  computer_cards = []

  is_game_over = False

  for _ in range(2):

    user_cards.append(deal_card())

    computer_cards.append(deal_card())

  while not is_game_over:

    user_score = calculate_score(user_cards)

    computer_score = calculate_score(computer_cards)

    print(f"   Your cards: {user_cards}, current score: {user_score}")

    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score>21:

      is_game_over = True

    else:

      another_card = input("Do you wish to draw another card, type y or n: ")

      if another_card == 'y':

        user_cards.append(deal_card())

      else:

        is_game_over = True

  while computer_score != 0 and computer_score < 17:

    computer_cards.append(deal_card())

    computer_score = calculate_score(computer_cards)

  print(f"Your cards are {user_cards} and your score is {user_score}")

  print(f"Computer's cards are {computer_cards} and thier score is {computer_score}")

  print(compare(user_score,computer_score))



  

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":

  clear()

  game()