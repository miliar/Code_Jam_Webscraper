#!/usr/bin/python3
import math
import itertools

def findExposed(pancakes):
    exposed = 0
    areas = []
    for index, p in enumerate(pancakes):
        areas.append(p[0])
        exposed += p[1]
    exposed += max(areas)
    return exposed


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    available, order = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case

    pancakes = []
    for j in range(available):
        rad, hei = [int(s) for s in input().split(" ")]
        area = rad * rad * math.pi
        pancakes.append((area, 2*math.pi * rad * hei))


    allpossible = itertools.combinations(pancakes, order)

    maxExp = 0
    for a in allpossible:
        temp = findExposed(a)
        if(temp > maxExp):
            maxExp = temp




    print("Case #{}: {}".format(i, str(maxExp)))