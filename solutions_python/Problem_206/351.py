def myspeed(d, d0, s):
    t = float(d - d0)/s
    return d/t

import sys
sys.setrecursionlimit(10000) 
if __name__ == "__main__":
    lines = open(sys.argv[1]).readlines()[1:]
    count = 1
    i = 0
    while i < len(lines):
        d, n = lines[i].strip().split(' ')
        d = float (d)
        n = int (n)

        horses = []
        speed = 99999999999999999.0
        for horse in range(i+1, i+n+1):
            d0, s = lines[horse].strip().split(' ')
            d0 = float(d0)
            s = float(s)
            speed = min(speed, myspeed(d, d0, s))
        i = i + n + 1
        print "Case #%d: %f" % (count, speed)
        count += 1
        
