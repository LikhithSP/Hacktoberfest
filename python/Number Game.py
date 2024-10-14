import random
secret = random.randint(0, 10)
count = 1
print("-------Guess The Number Game-------------")
while True:
    guess = int(input("Guess the number (0-10)>> "))
    if guess == secret:
        print('You Guessed it right.Victory!!')
        break
    else:
        print("Wrong!! Please Try Again")
        count += 1

print(f'You took {count} chances to guess')
