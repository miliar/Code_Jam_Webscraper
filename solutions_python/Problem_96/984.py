import sys
import numpy as np

def printsol(a,b,c):
    print a,b,c, "=", a+b+c


def dancenote(nbdancer, suprizingnb, minscore, scores):
    #print suprizingnb, minscore
    normalnotes = []
    surpnotes = []
    for s in scores:
        remain =  s % 3
        x = (s-remain) /3
        if x == 0:
            normal = min(remain,1) # 0,0,0  # 0,1,0 # 1,1,0
            supr = remain #0,0,0 # 0,1,0 # 2,0,0
        elif remain == 0:
            normal = x 
            #printsol(x, x, x)
            supr = x + 1
            #printsol(x-1, x, x+1)
        elif remain == 2:
            normal = x+1
            #printsol(x+1, x+1, x)
            supr = x+2 
            #printsol(x+2, x, x)
        else:
            normal = x+1 
            #printsol(x+1, x, x)
            supr = x+1 
            #printsol(x+1, x+1, x-1)
        normalnotes.append(normal)
        surpnotes.append(supr)

    normalnotes = np.array(normalnotes)
    surpnotes = np.array(surpnotes)
    goodnormal = normalnotes >= minscore
    goodsurp = (~goodnormal) & (surpnotes >= minscore)
    nbnormal = np.sum(goodnormal)
    nbsurp = np.sum(goodsurp)
    if nbsurp <= suprizingnb:
        return nbnormal + nbsurp
    else:
        return nbnormal + suprizingnb
        
fd = open(sys.argv[1])
n = fd.readline()
for n, l in enumerate(fd.readlines()):
    vals = [int(i) for i in l.split()]
    nbok = dancenote(vals[0], vals[1], vals[2], vals[3:])
    print "Case #%s: %s" % (n+1, nbok)
