# Google Code Jam Contest
# @L01cDev
# Author: Loic Boyeldieu
# Date: 08-04-2017

def isCorrectlyFlipped(pancakes):
    for p in pancakes:
        if p != "+":
            return False
    return True

def solvePancake(pancakes, K):
    index = 0
    counter = 0
    pancakes = [s for s in pancakes]
    while index+K<=len(pancakes):
        if pancakes[index]=="+":
            index+=1
        else:
            for i in range(K):
                if pancakes[index+i]=="+":
                    pancakes[index+i]="-"
                else:
                    pancakes[index+i]="+"
            index += 1
            counter += 1
    if isCorrectlyFlipped(pancakes):
        return counter
    else:
        return "IMPOSSIBLE"


T = int(input())
for i in range(1, T + 1):
    pancakes, K = raw_input().split(" ")
    K = int(K)

    result = solvePancake(pancakes, K)
    print("Case #{}: {}".format(i, result))
