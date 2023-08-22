guess = 0

while guess != 6:
  guess = int(input("Guess the number:  "))

print("You got it!")

if guess != 6:
  print('You ran out of tries.')
else:
  print('You got it!')
