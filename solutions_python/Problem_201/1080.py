import math

def parent(number):
    return math.floor(number/2)

def maxmin(gap):
    #max = math. ceil(gap/2)
    min = (gap-1)//2
    max = gap-1-min
    return max, min

t = int(input())

for i in range(1, t + 1):

    input_line = input().split()
    n = int(input_line[0])
    k = int(input_line[1])

    current = k
    path = []

    test = True
    if current == 1:
        test = False
    while test == True:
        if current % 2 == 0:
            path += ["max"]
        else:
            path += ["min"]
        current = parent(current)
        #print(current)
        if current == 1:
            test = False

    #print(path)

    while len(path) > 0:
        #print(path)
        max, min = maxmin(n)
        #print("max, min", max, min)
        if path[0] == "max":
            n = max
        else:
            n = min
        path = path[1:]
        #print("selected", n)

    max, min = maxmin(n)

    print("Case #{}: {} {}".format(i, max, min))

