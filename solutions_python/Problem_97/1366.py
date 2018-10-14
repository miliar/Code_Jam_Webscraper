from time import time
import math

start = 0

def startTimer():
    global start
    start = time()

def elapsed():
    return time() - start

def cyclesIn(A, B):
    count = 0
    for num in range(A, B):
        count += biggerCycles1(num, B)
    return count

def biggerCycles(num, B):
    string = str(num)
    n = len(string)
    count = 0
    seen = {}
    for i in range(n - 1):
        string = string[-1] + string[:n - 1]
        if num < int(string) <= B and string not in seen:
            count += 1
            seen[string] = 1
    return count

def biggerCycles1(num, B):
    if num <= 0:
        return 0
    n = int(math.log(num, 10)) + 1
    count = 0
    newNum = num
    seen = {}
    for i in range(n - 1):
        first = int(newNum / 10**(n - 1))
        newNum = 10 * (newNum - 10**(n - 1) * first) + first
        if num < newNum <= B and newNum not in seen:
            count += 1
            seen[newNum] = 1
    return count


def run():
    f = open('C-large.in', 'r')
    lines = f.readlines()
    f.close()
    data = [line.strip().split(' ') for line in lines]
    cases = int(lines[0])
    counter = 1

    g = open('CLanswers.txt', 'w')

    for i in range(cases):
        [A, B] = data[counter]
        g.write('Case #' + str(counter) + ': ' + str(cyclesIn(int(A), int(B))) + '\n')
        counter += 1

    g.close()

def test(n):
    startTimer()
    for i in range(n):
        cyclesIn(0, 1600000)
    print elapsed()
