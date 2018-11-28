#!/usr/bin/env python

#TEST = """3
#1
#3
#4
#1 2 1 2
#1
#4"""
#input = iter(open("B-small-attempt1.in")).__next__


def eat(layout):
    return [p-1 for p in layout if p>1]

memo = {}
def best(layout):
    # fastest time you can get p pancakes eaten...
    # divide the largest or wait?

    layout = tuple(sorted(layout))
    if layout in memo:
        return memo[layout]
    p = layout[-1]

    if p > 3:

        minimum = 1+best(eat(layout))
        pc = p
    
        for remainder in range(1,(pc//2)+1):
            divp = pc - remainder
            assert(remainder + divp == pc)
            split_layout = list(layout[:-1]) + [remainder, divp]
            split_cost = 1+best(split_layout)
            if split_cost < minimum:
                minimum = split_cost

        r = minimum

    elif p == 3:
        r = 3
    elif p == 2:
        r = 2
    elif p == 1:
        r = 1
    elif p == 0:
        r = 0

    memo[layout] = r
    return r

T = int(input())
for case in range(1, T+1):
    D = int(input())
    P = [int(d) for d in input().split()]
    assert(len(P) == D)

    #print("Case %s: ##### %s" % (case, P))
    print("Case #%s: %s" % (case, best(P)))
#import pdb;pdb.set_trace()


