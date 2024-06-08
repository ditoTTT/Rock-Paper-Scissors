import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
names = ['rock', 'paper', 'scissors']

computer = random.randint(0,2)
player = int(input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if player == 0 and computer == 1:
    print(f"You chose rock{rock}And Computer chose paper. {paper} You lose.")
elif player == 0 and computer == 2:
    print(f"You chose rock{rock}And Computer chose scissors. {scissors} You Win.")
elif player == 1 and computer == 0:
    print(f"You chose paper {paper}And Computer chose rock. {rock} You Win.")
elif player == 1 and computer == 2:
    print(f"You chose paper {paper}And Computer chose scissors. {scissors} You Lost.")
elif player == 2 and computer == 0:
    print(f"You chose scissors {scissors}And Computer chose rock. {rock} You Lost.")
elif player == 2 and computer == 1:
    print(f"You chose scissors {scissors}And Computer chose papers. {paper} You Win.")
else:
    print(f'You Both Chose {names[player]} {choices[player]}. Draw af!')


