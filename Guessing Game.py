secert_number = 9
guess_count = 0
total_guess = 3
while guess_count < total_guess:
   your_guess = int(input("Guess: "))
   guess_count += 1
   if your_guess == secert_number:
      print("You Win!")
      break
   else:
       print("Sorry! You loss this match. Better luck next time.")

print("Thanks for playing this game. Created by Anuraj Kumar Dwivedi with ❤.")

