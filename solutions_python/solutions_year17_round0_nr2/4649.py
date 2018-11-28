#!/usr/bin/python3
#-*- coding: utf-8 -*-

def IsSorted(n):
    n = str(n)
    if len(n) == 1:
        return True
    for i in range(len(n)-1):
        if int(n[i]) > int(n[i+1]):
            return False
    return True

if __name__ == "__main__":
    # Read nb inbut
    nbExec = int(input())
    for i in range(nbExec):
        n = int(input())
        j = n
        while (not IsSorted(j)):
            j-=1
        print ("Case #{}: {}".format(i+1,j))
