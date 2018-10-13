import math

num_tries = int(input())

for j in range(num_tries):

    num_stalls, num_people = input().split(' ')
    num_stalls = int(num_stalls)
    num_people = int(num_people)

    if (num_people == 1):
        big = num_stalls // 2
        small = (num_stalls - 1) // 2
        print("Case #" + str(j+1) + ": " + str(big) + " " + str(small))
        continue

    lg = math.floor(math.log(num_people, 2))    
    size = math.ceil((num_stalls - 2**lg + 1) / 2**lg)
    if (size == 1):
        big = 0
        small = 0
        print("Case #" + str(j+1) + ": " + str(big) + " " + str(small))
        continue

    amount_big = ((num_stalls - 2**lg + 1)%2**lg)
    if (amount_big == 0):
        amount_big = 2**lg
    if (num_people - 2**lg + 1 > amount_big):
        size = size - 1

    big = size // 2
    small = (size - 1) // 2
    
    print("Case #" + str(j+1) + ": " + str(big) + " " + str(small))
    
