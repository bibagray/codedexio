# magic 8 ball 💖
import random
question = input('')
random_number = random.randint(1,9)
if random_number == 1:
  answer = 'Yes - definitely'
elif random_number == 2:
  answer = 'It is decidedly so'
elif random_number == 3:
  answer = 'Without a doubt'
elif random_number == 4: 
  answer = 'Reply hazy, try again'
elif random_number == 5:
  answer = 'ask again later'
elif random_number == 6:
  answer = 'better not tell you now'
elif random_number == 7:
  answer = 'my sources say no'
elif random_number == 8:
  answer = 'outlook not so good'
elif random_number == 9:
  answer = 'very doubtful'
else:
  answer = 'error'
print('Question: + question')
print('Magic 8 ball: + answer')
