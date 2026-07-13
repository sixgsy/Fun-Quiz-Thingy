print('Solar System Quiz')

input('Name: ')
input('Section: ')

correct = 'You are correct!'

wrong = 'You are incorrect!'

score = 0

q1 = input('Is Pluto still a planet? (T/F): ')

if q1 == "T":
    print(correct)
    score = +1

elif q1 == "F":
    print(wrong)

else:
    print ('You are incorrect!')

q2 = input('Is mercury the hottest planet in our Solar System? (T/F): ')

if q2 == "F":
    print(correct)
    score = +1

elif q2 == "T":
    print(wrong)

else:
    print ('You are incorrect!')

q3 = input('Is our Sun being eaten by astrophages? (T/F): ')

if q3 == "T":
    print(correct)
    score = +1

elif q3 == "F":
    print(wrong)

else:
    print ('You are incorrect!')

q4 = input('Did the Big Bang happen yesterday? (T/F): ')

if q4 == "F":
    print(correct)
    score = +1

elif q4 == "T":
    print(wrong)

else:
    print ('You are incorrect!')

q5 = input('Am I handsome? (T/F): ')

if q5 == "T":
    print(correct)
    score = +1

elif q5 == "F":
    print('Invalid Answer.')

else:
    print ('You are incorrect!')

answers = q1 + q2 +q3 + q4 + q5

result = (len(answers) * 20)

print(f'Your score is: {result}%')


