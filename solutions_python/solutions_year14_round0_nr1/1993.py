#!/usr/bin/env python

from sys import argv

with open(argv[1]) as f:
    nCases = int(f.next())
    out = []
    ansStr = "Case #{}: {}"
    for _ in xrange(nCases):
        a1 = int(f.next())
        for i in range(4):
            row = f.next()
            if i+1 == a1:
                row1 = map(int, row.split())
        a2 = int(f.next())
        for i in range(4):
            row = f.next()
            if i+1 == a2:
                row2 = map(int, row.split())
        goodcards = 0
        answer = None
        for num in row1:
            if num in row2:
                goodcards += 1
                answer = num
        if goodcards==0:
            out.append(ansStr.format(_+1, "Volunteer cheated!"))
        elif goodcards==1:
            out.append(ansStr.format(_+1, answer))
        else:
            out.append(ansStr.format(_+1, "Bad magician!"))
        
with open('magic_trick.out', 'w') as outf:
    for s in out:
        outf.write(s + "\n")
