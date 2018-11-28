lines = open("a-large.txt").read().split("\n")
T = int(lines[0])

def f(st):
    sofar = 0
    to_add = 0
    for i,a in enumerate(st):
        if sofar < i:
            to_add += 1
            sofar += 1
        
        sofar += int(a)
    return to_add

for i in xrange(1,T+1):
    out = f(lines[i].split(" ")[-1])
    print "Case #%d: %d" % (i, out)