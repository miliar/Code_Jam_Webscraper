#!/usr/bin/env python
z = int(raw_input())

for case in xrange(1,z+1):
    A, N = map(int,raw_input().split())
    motes = map(int,raw_input().split())
    moves = 0
    while(motes):
        new_motes = []
        summ = 0
        for i in motes:
            if i < A:
                summ += i
            else:
                new_motes.append(i)
        
        if len(motes) == len(new_motes):
            if A < 2:
                moves += len(new_motes)
                break
            B = min(new_motes)
            AA = A
            res = 0
            while AA <= B:
                AA += AA-1
                res += 1
            if res < len(new_motes):
                moves += res
                A = AA
            else:
                moves += len(new_motes)
                break
            
        motes = new_motes
        A += summ
        
    print "Case #" + str(case) + ": " + str(moves)
