import math

def fill_next(i, v):
    for j in range(i, len(v)):
        v[j] = 9

t = int(raw_input())



for line in xrange(1, t + 1):
    n = int(raw_input())
    list_n = [int(c) for c in str(n)]
    tie = 0
    for i in range(1, len(list_n)):
        if list_n[i] < list_n[i-1]:
            list_n[i-tie-1] -= 1
            fill_next(i-tie, list_n)
            break
        elif list_n[i] == list_n[i-1]:
            tie += 1
        else:
            tie = 0
    lenght = len(list_n) - 1
    result = 0
    for i, j in enumerate(list_n):
        result += j* int(math.pow(10, (lenght-i)))
    print "Case #{}: {}".format(line, result)
