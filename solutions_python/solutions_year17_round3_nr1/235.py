from decimal import *
import sys
from math import sqrt
from math import pi
from collections import deque
import heapq
#my_dict.pop('key', None)
sys.setrecursionlimit(1500)
in_file = open('A-large.in', 'r')
out_file = open('A-large-answer.in', 'w')


def solve(all, pancake):
    for i in range(len(pancake)):
        for j in range(len(pancake[i])):
            pancake[i][j] = float(pancake[i][j])
    pancake = mergere(pancake)
    for i in range(len(pancake)):
        k = pancake[i][0] * 2 * pi * pancake[i][1]
        pancake[i].append(k)
    choose = int(all[1])
    answer = 0
    for i in range(len(pancake) - 1, -1, -1):
        first = pancake[i]
        if len(pancake[:i]) < choose - 1:
            break
        else:
            new = list(pancake[:i])
            new = mergehe(new)
            a = choose - 1
            j = 0
            temp = 0
            while a > 0:
                temp += new[-1 - j][2]
                a -= 1
                j += 1
            temp += pancake[i][2]
            temp += pi * (pancake[i][0] ** 2)
            answer = max(answer, temp)
    return answer

def mergere(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        A = mergere(arr[:len(arr) // 2])
        B = mergere(arr[len(arr) // 2:])
        p = merging(A, B)
        return p

def merging(arrA, arrB):
    i = 0
    j = 0
    arr = []
    while True:
        try:
            if arrA[i][0] <= arrB[j][0]:
                arr.append(arrA[i])
                i += 1
            else:
                arr.append(arrB[j])
                j += 1
        except:
            if i == len(arrA):
                arr = arr + arrB[j:]
            else:
                arr = arr + arrA[i:]
            break
    return arr

def mergehe(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    else:
        A = mergehe(arr[:len(arr) // 2])
        B = mergehe(arr[len(arr) // 2:])
        p = merg(A, B)
        return p

def merg(arrA, arrB):
    i = 0
    j = 0
    arr = []
    while True:
        try:
            if arrA[i][2] <= arrB[j][2]:
                arr.append(arrA[i])
                i += 1
            else:
                arr.append(arrB[j])
                j += 1
        except:
            if i == len(arrA):
                arr = arr + arrB[j:]
            else:
                arr = arr + arrA[i:]
            break
    return arr

p = []
for line in in_file:
    p.append(line)
n = p[0]
q = 1
i = 1
answer = None
ques = []
getcontext().prec = 30
while q < len(p):
    onelinelist = p[q].strip().split()
    two = []
    for qwe in range(int(onelinelist[0])):
        q += 1
        temp = p[q].strip().split()
        two.append(temp)
    answer = solve(onelinelist, two)
    print("Case #%d: " % (i) + str(answer))
    out_file.write("Case #%d: " % (i) + str(answer) + '\n')
    i += 1
    q += 1