#!/usr/bin/env python

def case(T):
    d, n = map(int, input().split())
    horses = [tuple(map(int,input().split())) for i in range(n)]
    #print(d, horses)
    times = [(d-p)/s for p, s in horses]
    T = d/max(times)
    return T

if __name__=="__main__":
    for i in range(int(input())):
        print("Case #{}: {}".format(i+1, case(i)))
