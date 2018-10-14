import sys
import math

input = sys.stdin.readline()
num = int(input)

number = 1
power = []
while number < 1000000:
    power.append(number)
    number *= 2

def summation(vec):
    total = 0
    for item in vec:
        total += item
    return total

for iter in range(0, num):
    input = sys.stdin.readline()
    count = int(input)
    input = sys.stdin.readline()
    element = input.split()
    count = len(element)
    candy = []
    for item in element:
        candy.append(int(item))
    candy.sort()
    maxx = candy[-1]
    for maxPow in range(0, len(power)):
        if maxx < power[maxPow]:
            break
    success = 1
    for i in range(0, maxPow):
        total = 0
        for j in range(0, count):
            if candy[j] / power[i] % 2:
                total += 1
        if total % 2:
            success = 0
            break
    print "Case #%d:" % (iter + 1),
    if not success:
        print "NO"
    else:
        print summation(candy) - candy[0]
