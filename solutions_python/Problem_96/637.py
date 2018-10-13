
import sys

supr = [(x,y,z) for x in range(0,11) for y in range(0,11)
        for z in range(0,11) if x>=y>=z and max(x,y,z)-min(x,y,z)==2]
nosupr = [(x,y,z) for x in range(0,11) for y in range(0,11)
        for z in range(0,11) if x>=y>=z and max(x,y,z)-min(x,y,z)<2]
#print supr
#print nosupr

def fns(xs, p):
    """Filter n sum"""
    return map(lambda (x,y,z):x+y+z,
            filter(lambda (x,y,z):x>=p,xs))
def fnsLESS(xs, p):
    """Filter n sum"""
    return map(lambda (x,y,z):x+y+z,
            filter(lambda (x,y,z):x<p,xs))

T = int(sys.stdin.readline())



for i in range(1,T+1):
    #p_supr / p_no supr / supr / nosupr
    c10__ = 0
    c11__ = 0
    c010_ = 0
    c011_ = 0
    c0011 = 0
    c0001 = 0
    
    line = sys.stdin.readline().split()
    line = map(lambda x : int(x), line)
    #print line
    minsup = 0
    maxsup = 0 # incl
    above_p = 0
    p = line[2]
    for t in line[3:]:
        if t in fns(supr,p) and not t in fns(nosupr,p):
            c10__ += 1
        elif t in fns(supr,p) and t in fns(nosupr,p):
            c11__ += 1
        elif not t in fns(supr,p) and t in fns(nosupr,p) and not t in fnsLESS(supr,p):
            c010_ += 1
        elif not t in fns(supr,p) and t in fns(nosupr,p) and t in fnsLESS(supr,p):
            c011_ += 1
        elif t in fnsLESS(supr,p) and t in fnsLESS(nosupr,p):
            c0011 += 1
        elif not t in fnsLESS(supr,p) and t in fnsLESS(nosupr,p):
            c0001 += 1
        else:
            raise Exception

    s = line[1]
    cp = 0

    while c10__+c11__+c011_+c010_+c0011+c0001>0:
        if s > 0 and c10__>0:
            s-=1
            c10__-=1
            cp+=1
        elif s>0 and c11__>0:
            c11__-=1
            s-=1
            cp+=1
        elif s>0 and c0011>0:
            c0011-=1
            s-=1
            cp+=0
        elif s>0 and c011_>0:
            c011_-=1
            s-=1
            cp+=0
        elif s>0:
            raise Exception
        else:
            cp+= c11__+c011_+c010_
            break
    print "Case #" + str(i) + ": " + str(cp)





