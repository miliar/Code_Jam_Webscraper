T = int(input())

for t in range(T):
    firstrow = int(input())
    firstpossible = set([[int(x) for x in input().split()] for i in range(4)][firstrow - 1])
    secondrow = int(input())
    secondpossible = set([[int(x) for x in input().split()] for i in range(4)][secondrow - 1])
    inter = firstpossible.intersection(secondpossible)
    message = ""
    if (len(inter) == 0):
        message = "Volunteer cheated!"
    elif (len(inter) > 1):
        message = "Bad magician!"
    else:
        message = "{0}".format(inter.pop())
    print("Case #{0}: {1}".format(t + 1, message))
