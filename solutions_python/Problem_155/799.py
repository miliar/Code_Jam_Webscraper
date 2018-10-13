#!/bin/python

T = int(input())

for j in range(T):
    _, data = input().split()
    guests = 0
    stands = 0
    i = 0
    for c in data:
        if i > stands :
            dguests = i - stands
            guests += dguests
            stands += dguests
        
        stands += int(c)
        i += 1
    print ("Case #%d: %d" % (j+1, guests))

