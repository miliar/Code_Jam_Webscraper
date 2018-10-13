import sys

def calcPos(pos, l, minV):
    num = 0
    t = len(pos)
    old_p = -1
    for p in pos:
        bp = 0
        ap = 0
        if p > 0:
            bp = p - old_p - 1
        if (p + minV) < l:
            ap = l - (p+minV)

        if bp == 0 or ap == 0:
            total = bp + ap + 1
        else:
            total = (bp+1) * (ap+1)

        num += total
        old_p = p

    return num 
            
def consonantsValue(s, minV):
    l = len(s)
    pos = []
    vowels = ['a','e','i','o','u'] 

    for i in xrange(l-minV+1):
        t = 0
        c = True
        for j in xrange(minV):
            if s[i+j] in vowels:
                c = False
                break
                 
        if c == True:
            pos.append(i)

    num = calcPos(pos, l, minV)
    return num 

if __name__ == '__main__':
    lines = int(raw_input())
    for i in xrange(lines):
        line = raw_input().split()
        print "Case #%s: %s"%(i+1, consonantsValue(line[0], int(line[1])))
