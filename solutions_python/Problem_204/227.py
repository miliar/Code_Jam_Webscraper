#!/usr/bin/env python3
import itertools


T = int(input())

def solve(casei):
    line = input().split(" ")
    N = int(line[0])
    P = int(line[1])
    one_serving = [int(x) for x in input().split()]
    quantity = []
    for i in range(N):
        quantity.append([int(x) for x in input().split()])
    #print(one_serving)
    #print(quantity)

    # brute force
    ans = -1
    if N == 1:
        ans = 0
        for i in range(P):
            guess_max = (quantity[0][i] * 100) // (one_serving[0] * 90)
            guess_min = (quantity[0][i] * 100) // (one_serving[0] * 110)
            for guess in range(guess_min, guess_max+1):
                if (quantity[0][i] * 100 <= one_serving[0] * 110 * guess) and (quantity[0][i] * 100 >= one_serving[0] * 90 * guess):
                    ans += 1
                    break
    elif N == 2:
        ans_max = 0
        quantity[0].sort()
        quantity[1].sort()
        for item in list(itertools.permutations(quantity[1])):
            ans = 0
            for i in range(P):
                guess_max = (quantity[0][i] * 100) // (one_serving[0] * 90)
                guess_min = (quantity[0][i] * 100) // (one_serving[0] * 110)
                for guess in range(guess_max, guess_min-1, -1):
                    good = 1
                    if (quantity[0][i] * 100 > one_serving[0] * 110 * guess):
                        good = 0
                    if (quantity[0][i] * 100 < one_serving[0] * 90 * guess):
                        good = 0
                    if (item[i] * 100 > one_serving[1] * 110 * guess):
                        good = 0
                    if (item[i] * 100 < one_serving[1] * 90 * guess):
                        good = 0
                    if good == 1:
                        ans += 1
                        break
            if ans > ans_max:
                ans_max = ans
            if ans_max == P:
                break
        ans = ans_max
    print("Case #{}: {}".format(casei, ans))

for i in range(1, T+1):
    solve(i)
