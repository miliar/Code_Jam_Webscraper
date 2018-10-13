import sys


def process(chaine, smax):
    lst = [int(i) for i in chaine]
    toappend = 0
    cumul = 0
    for i,v in enumerate(lst):
        if v==0: continue
        if cumul < i:
            toappend+= i-cumul
            cumul+=toappend
        cumul += v
    return toappend


if __name__=="__main__":
    T = int(sys.stdin.readline())
    for t in range(T):
        line = sys.stdin.readline()
        lspl = line.split()        
        print "Case #%i: %i"%(t+1,process(lspl[1], int(lspl[0])))
                