#!/usr/bin/python
import sys

def solve(inp):
    data = inp.split('\n')
    tests = int(data[0])
    outp = ''
    for i in range(tests):
        line = data[1 + i].split(' ')
        msi = line[0]
        people = line[1]
        needed = 0
        standing = 0
        for k in range(len(people)):
            while standing < k:
                needed += 1
                standing += 1
            standing += int(people[k])
        outp += 'Case #%d: %d\n' % (i+1, needed)
    return outp.strip()

data = open(sys.argv[1]).read()
o = solve(data)
print o
f = open(sys.argv[2], 'w')
f.write(o)
f.close()

