import string
from math import sqrt
from math import ceil

def checkrec(number):
    length = len(number)
    for i in range(0, int(length / 2)):
        if number[i] != number[-(i + 1)]:
            return False
    return True

def search(a, b):
    count = 0
    for i in range(a, b + 1):
        if checkrec(str(i)):
            if checkrec(str(i * i)):
                count += 1
    return count

T = int(input())

for TT in range(1, T + 1):
    a, b = input().split()
    a = int(a)
    b = int(b)
    a = ceil(sqrt(a))
    b = int(sqrt(b))
    print("Case #" + str(TT) + ": " + str(search(a, b)))


