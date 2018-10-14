#!/usr/bin/env python3

def case(T):
    pancakes, K = input().strip().split()
    K = int(K)
    pancakes = list(pancakes)
    P = len(pancakes)
    #print(pancakes)
    count = 0
    for i in range(P-K+1):
        if pancakes[i] == "-":
            count += 1
            flip(pancakes, i, K)
    #print("end", pancakes)
    if "".join(pancakes) == '+'*P:
        return count
    else:
        return "IMPOSSIBLE"


def flip(pin, ploc, K):
    for i in range(K):
        pin = inv(pin, ploc+i)
    return pin

    
def inv(a, p):
    if a[p] == "-":
        a[p] = "+"
    else:
        a[p] = "-"
    return a

if __name__=="__main__":
    for i in range(int(input())):
        print("Case #{}: {}".format(i+1, case(i)))
