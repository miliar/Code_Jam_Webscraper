#!/usr/bin/python

SIZE = 'small'
PROBLEM = 'C'
DATASET = PROBLEM + '-' + SIZE
IFILE = DATASET + '.in'
OFILE = DATASET + '.out'

def touches(r1, r2):
    return (
            r1[0] <= r2[2]+1 and r2[0] <= r1[2]+1
            ) and (
            r1[1] <= r2[3]+1 and r2[1] <= r1[3]+1
            )

def solve_group(group):
    left = min(x1+y1 for x1,y1,x2,y2 in group)
    right = max(x2 for x1,y1,x2,y2 in group) + max(y2 for x1,y1,x2,y2 in group)
    return right-left+1

def solve(rects):
    groups = [i for i in xrange(len(rects))]
    for rect1 in xrange(len(rects)):
        for rect2 in xrange(rect1+1, len(rects)):
            if touches(rects[rect1], rects[rect2]):
                old = max(groups[rect1], groups[rect2])
                new = min(groups[rect1], groups[rect2])
                groups = [new if a==old else a for a in groups]
    grouped = [[] for i in xrange(max(groups)+1)]
    for i in xrange(len(groups)):
        grouped[groups[i]].append(rects[i])
    grouped = [a for a in grouped if len(a)]
    print grouped
    return max(solve_group(group) for group in grouped)

ifile = open(IFILE, 'r')
ofile = open(OFILE, 'w')
C = int(ifile.readline())
for i in xrange(C):
    R = int(ifile.readline())
    rects = []
    for j in xrange(R):
        line = ifile.readline().strip().split(' ')
        rects.append([int(a) for a in line])
    solution = solve(rects)
    ofile.write('Case #%s: %s\n' % (i+1,str(solution)))
ifile.close()
ofile.close()
