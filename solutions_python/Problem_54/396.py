import time

start_time = time.time()

def gcd_all(x):
    # returns the gcd of the list of numbers
    return reduce(gcd, x)

def gcd2_all(x):
    # returns the gcd of the list of numbers
    return reduce(gcd2, x)

def gcd(x, y):
    while x <> y and x > 1 and y > 1:
        if x > y:
            x -= y
        else:
            y -= x

    # needed in case y is 1
    if x == 1 or y == 1:
        return 1

    return x

def gcd2(x, y):
    while 1:
        if x == 0: return y
        if y == 0: return x

        if x > y:
            x, y = y, x - y * (x/y) # int division
        else:
            y, x = x, y - x * (y/x) # int division

def find(x):
    # finds k to maximise gcd(x[0]+k, x[1]+k, x[2]+k, ...)

    x2 = list(set(x)) # remove duplicates, order unimportant
    
    # find first order difference
    diff = []
    for i in range(len(x2)-1):
        diff.append(abs(x2[i+1] - x2[i]))

    # find gcd of diff
    g = gcd2_all(diff)
    
    # find k
    k = x[0] - g * (x[0]/g) # relies on integer division, this is how much to subtract
    if k <> 0:
        k = g - k # how much to add

    return k


f = open("B-large.in", "r")
f2 = open("B-large.out", "w")

try:
    lines = f.readlines()
    C = int(lines[0].strip())

    line = []
    for i in range(1, C+1):
        line = map(int, lines[i].strip().split(" ")[1:]) # skip first number

        # k = find(line)
        # l2 = map(lambda x: x+k, line)
        # print "With numbers %s, add %d to get %s and gcd2 = %d (gcd = %d)" % (line, k, l2, gcd2_all(l2), gcd_all(l2))
        
        s = "Case #%d: %d\n" % (i, find(line))
        f2.write(s)

    f2.flush()
     
except Exception, ex:
    print ex
    
finally:
    f.close()
    f2.close()



print "time = %f seconds" % (time.time() - start_time)
