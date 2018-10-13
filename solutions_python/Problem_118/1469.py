import math

lines = [line.strip() for line in open('small_input.txt').readlines() if line.strip()]
num_cases = int(lines[0])

def ispal(n):
    n = str(n)
    return all([n[i]==n[-1-i] for i in range(len(n)/2)])

def num_fsq(low, high):
    ct = 0
    sqrtlow = int(math.sqrt(low-1))+1
    sqrthigh = int(math.sqrt(high))
    for i in range(sqrtlow, sqrthigh+1):
        if ispal(i):
            if ispal(i*i):
                ct += 1
    return ct

for i in range(1, len(lines)):
    line = lines[i].split()
    low, high = int(line[0]), int(line[1])
    print 'Case #%i: %i' % (i, num_fsq(low, high))
