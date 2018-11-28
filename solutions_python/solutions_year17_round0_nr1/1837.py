#Joe Snider
#4/16
#
#code jam 2017, qual A

def flip(c):
    if c == '-':
        return '+'
    return '-'

def check(griddle):
    for s in griddle:
        if s == '-':
            return False
    return True

def flipall(griddle, n):
    flips = 0
    for i in range(len(griddle)-n+1):
        if griddle[i] == '-':
            #print griddle
            for j in range(i, i+n):
                griddle[j] = flip(griddle[j])
            #print griddle
            flips += 1
    if check(griddle):
        return str(flips)
    return 'IMPOSSIBLE'
    
#raw_imput is one line    
t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input().split(" ")
    griddle = [x for x in line[0]]
    n = int(line[1])
    print "Case #%d: %s"%(i, flipall(griddle, n))
