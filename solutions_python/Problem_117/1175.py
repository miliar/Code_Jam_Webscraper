import sys


def check_line(row, col, pattern):
    target = pattern[row][col]
    c = True
    r = True
    width = len(pattern[0])
    height = len(pattern)
    # check column line
    for i in xrange(height):
        if pattern[i][col] > target:
            c = False
            break
    # check row line
    for j in xrange(width):
        if pattern[row][j] > target:
            r = False
            break
    return c or r

def check(pattern):
    for i in xrange(len(pattern)):
        for j in xrange(len(pattern[0])):
            if not check_line(i, j, pattern):
                return 'NO'
    return 'YES'

input = sys.argv[1]
with open(input) as f:
    lines = f.readlines()
size = int(lines[0])
lines = lines[1:]
for i in xrange(size):
    size = [int(j) for j in lines[0].split()]
    patternStr = lines[1:size[0] + 1]
    pattern = []
    for l in patternStr:
        pattern.append([int(n) for n in l.split()])
    lines = lines[size[0] + 1:]
    ret = check(pattern)
    print "Case #" + str(i+1) + ": " + ret