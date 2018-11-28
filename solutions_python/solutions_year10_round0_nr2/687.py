from __future__ import division

case = 0

def gcd(a,b):
        if a==0 or b==0: 
                return 0
        while max(a,b)%min(a,b)!=0:
                if b>a: a,b= b,a
                a -=b
        if b>a: a,b= b,a
        return b

for line in [l for l in file("in")][1:]:
        case +=1 
        line = [int(i) for i in line.split(" ")][1:]
        least = min(line)
        line = [i-least for i in line if i != least]
        line = reduce(gcd, line)
        if least % line == 0:
                res = 0
        else:
                res = line - least % line
        print "Case #%d: %d" % (case, res)

