
a = ['+', '-', '-', '-', '+']

def makelist(x):
    total = []
    for i in x:
        total.append(i)
    return total

def flip(x, start, size):
    for i in range(size):
        if x[start+i] == '+':
            x[start+i] = '-'
        else:
            x[start+i] = '+'



    

def answer(s, k):
    b = len(s)
    total = 0
    for i in range(b-k+1):
        if s[i] != '+':
            flip(s, i, k)
            total += 1
    for j in range(b):
        if s[j] != '+':
            return "IMPOSSIBLE"
    return total









    


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, k = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
  a = makelist(n)
  b = int(k)
  print("Case #{}: {}".format(i, answer(a, b)))
  # check out .format's specification for more formatting options















"""


def tidy(x):
    i = x % 10
    x //= 10
    while x != 0:
        if i < (x % 10):
            return False
        i = x % 10
        x //= 10
    return True

def repeat(x, y):
    total = 0
    while y > 0:
        total += x
        x *= 10
        y -= 1
    return total

def digit(x):
    total = 0
    while x != 0:
        total += 1
        x //= 10
    return total


def answer(x):
    total = 0
    a = digit(x)
    b = 10 ** (a-1)
    c = x // b
    d = repeat(c, a)
    if d > x:
        return (b*c)-1
    elif d == x:
        return x
    else:
        total = b*c
        return total + answer(x - b*c)

:(
"""
