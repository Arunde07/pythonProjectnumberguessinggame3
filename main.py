import random

secretnum = random.randint(1,50)
print(secretnum)
count = 1

while(True):
    guess = int(input("guess the number (1-50) >> "))
    if guess==secretnum:
        print("you guessed it right. victory!")
        break
    else:
        print("oh no! try again!")
        count += 1

print(f"you took {count} chances.")