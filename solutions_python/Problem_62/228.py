import os

def calc(n, lines):
    y = 0
    for i in xrange(n):
        for j in xrange(i + 1, n):
            if ((lines[i][0] < lines[j][0]) and (lines[i][1] > lines[j][1])) or ((lines[i][0] > lines[j][0]) and (lines[i][1] < lines[j][1])):
                y = y + 1
    return y

t = input()

for i in xrange(t):
    n = input()
    print "Case #%d:" % (i+1),
    lines = []
    for j in xrange(n):
        lines.append(map(int, raw_input().split()))
    print calc(n, lines)
    