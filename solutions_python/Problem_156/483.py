#!/usr/bin/env python3

import heapq

def calcEatTime(n):
    if n == 0:
        return 0
    return (n-1).bit_length() + 1

def calcDinersTime(diners):
    time1 = len(diners) - 1
    if time1 <= 3:
        return time1

    minTime = time1
    maxNum = diners[-1]
    i = 1
    while i * maxNum < time1:
        newDiners = diners[:]
        newDiners[-1] = 0
        newDiners[time1 // (i+1)] += maxNum * (i+1 - time1 % (i+1))
        newDiners[time1 // (i+1) + 1] += maxNum * (time1 % (i+1))

        while newDiners[-1] == 0:
            newDiners.pop()

        minTime = min(minTime, maxNum * i + calcDinersTime(newDiners))
        i += 1

    return minTime

def countDiners(diners):
    counter = [0] * (max(diners) + 1)
    for n in diners:
        counter[n] += 1
    return counter

def solve(diners):
    diners = countDiners(diners)
    return calcDinersTime(diners)

if __name__ == '__main__':
    for i in range(1, int(input())+1):
        input()
        diners = [int(x) for x in input().split()]
        time = solve(diners)
        print('Case #{0}:'.format(i), time)
