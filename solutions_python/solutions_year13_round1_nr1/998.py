import re
import sys
import math
import string


def main():
    output = []
    f = open('/home/mani/Downloads/A-small-attempt0.in', 'r')
    g = open('out.dat', 'w')
    g.close()
    data = f.readlines()
    f.close()
    numlines = int(data[0])
    for i in xrange(numlines):
        pair = data[i+1]
        r = long(pair.split()[0])
        t = long(pair.split()[1])
        cnt = 0
        tick = 1
        l = r+1
        m = r
        cnt = cnt + ((l**2)-(m**2))
        while cnt < t:
          l = l+2
          m = m+2
          cnt = cnt + ((l**2)-(m**2))
          #print r, t, cnt
          if cnt <= t:
            tick=tick+1
        #print tick
        
        outline = "Case #%d: %d\n" % (i+1, tick)
        #output.append(outline)
        with open("out.dat", "a") as myfile:
            myfile.write(outline)


if __name__ == "__main__":
    main()
