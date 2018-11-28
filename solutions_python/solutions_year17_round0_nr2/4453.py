from math import floor
from functools import reduce

def tidy(num):
    n = str(num)
    for i in range(len(n) - 1, 0, -1):
        if int(n[i]) < int(n[i-1]):
            return False
    return True


def last_tidy(num):
    if num < 10:
        return num
    n = list(map(int, str(num)))
    for i in range(len(n) - 1, 0, -1):
        if n[i] < n[i-1]:
            for j in range(i, len(n)):
                n[j] = 9
            n[i-1] -= 1
    return reduce(lambda x,y: x*10+y, n)

lines = [line.rstrip('\n') for line in open('B-large.in')]
n = int(lines[0])
for i in range(n):
    print('Case #{0}: {1}'.format(i+1, last_tidy(int(lines[i+1]))))