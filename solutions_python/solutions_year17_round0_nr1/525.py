#!/usr/bin/python3
# Python version >= 3.6

def flip(pancakes, K):
    count = 0
    # easiest is to mutate a list (and not to keep flip counters. S<=1000)
    pancakes = list(pancakes)
    for k in range(len(pancakes) - K + 1):
        if pancakes[k] == "-":
            count +=1
            toflip = pancakes[(k+1):(k+K)]
            flipped = ["+" if x=="-" else "-" for x in toflip]
            pancakes[(k+1):(k+K)] = flipped
    
    if all(x=="+" for x in pancakes[(-K+1):]):
        return count
    else:
        return "IMPOSSIBLE"



if __name__=="__main__":
    T = int(input())

    for case in range(T):
        pancakes, K = input().split()
        print(f"Case #{case+1}: {flip(pancakes, int(K))}")
        

