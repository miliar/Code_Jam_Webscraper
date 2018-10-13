import sys

f = map(str.strip, open(sys.argv[1], 'rb').readlines(), "\n")
n = int(f.pop(0))

def solve(c):
    org = [int(x[1]) for x in c if x[0]=='O']
    opos = 1
    blu = [int(x[1]) for x in c if x[0]=='B']
    bpos = 1
    t = 0
    while len(c) > 0:
        pushed = False
        if len(org) > 0:
            if org[0] != opos:
                opos += cmp(org[0] - opos, 0)
            elif c[0][0] == 'O':
                c.pop(0)
                org.pop(0)
                pushed = True

        if len(blu) > 0:
            if blu[0] != bpos:
                bpos += cmp(blu[0] - bpos, 0)
            elif c[0][0] == 'B' and not pushed:
                c.pop(0)
                blu.pop(0)
        t+=1
    return t

for i in range(n):
    l = f[i].split()[1:]
    c = zip(l[::2], map(int, l[1::2]))
    print "Case #%s: %s" % (i+1, solve(c))
