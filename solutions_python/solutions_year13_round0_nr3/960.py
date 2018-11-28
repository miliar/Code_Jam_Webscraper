import math


def solve(a, b):
    i = int(math.floor(math.sqrt(a)))

    sm = 0
    while i*i <= b:
        if i*i >= a:
            if isfands(i):
                sm += 1
        i += 1

    return sm


def isfands(n):
    return ispal(n) and ispal(n*n)

def ispal(n):
    strn = str(n)
    return (strn == strn[::-1])


inp = raw_input()
T = int(inp)
for t in range(1,T+1):
    inp = raw_input()
    A, B = map(int, inp.split(' '))
    answer = solve(A, B)
    print "Case #" + str(t) + ": " + str(answer)
