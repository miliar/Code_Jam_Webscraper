#!/usr/bin/env python

def hours_to_mins(x):
    depart, arrive = x.split(" ")
    hours, mins = [int(x) for x in depart.split(":")]
    depart = hours*60 + mins
    hours, mins = [int(x) for x in arrive.split(":")]
    arrive = hours*60 + mins
    return (depart, arrive)

def solution(T, from_a, from_b):
    # Sort based on departure time
    from_a.sort( lambda x,y : cmp(x[0], y[0]))
    from_b.sort( lambda x,y : cmp(x[0], y[0]))

    # Furthermore.. subtract the turnaround time from all of them
    from_a = [(ele[0]-T, ele[1]) for ele in from_a]
    from_b = [(ele[0]-T, ele[1]) for ele in from_b]

    # Trains we actually have in the state
    a = 0
    b = 0
    # Trains that we require from the start
    A = 0
    B = 0
    for minute in range(-2*T, 24*60):
        for trip in from_a:
            if trip[1] == minute:
                b = b + 1
        for trip in from_b:
            if trip[1] == minute:
                a = a + 1

        for trip in from_a:
            if trip[0] == minute:
                if a > 0:
                    a = a - 1
                else:
                    A = A + 1
        for trip in from_b:
            if trip[0] == minute:
                if b > 0:
                    b = b -1
                else:
                    B = B + 1
        # Next minute



    return A, B

N = int(raw_input())
for i in range(N):
    T = int(raw_input())
    NA, NB = [int(x) for x in raw_input().split(' ')]
    from_a = [raw_input() for j in range(NA)]
    from_b = [raw_input() for j in range(NB)]
    from_a = [hours_to_mins(x) for x in from_a]
    from_b = [hours_to_mins(x) for x in from_b]
    sA, sB = solution(T, from_a, from_b)
    print "Case #%i: %i %i" % (i+1, sA, sB)
