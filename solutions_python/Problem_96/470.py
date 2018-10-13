from sys import argv

def maxBest(p,S,l):
    ret=0
    l=[x for x in l if x>=p]
    for score in l:
        if (score+2)/3 >= p:
            ret +=1
        elif S>0 and (score+4)/3 >=p:
            ret +=1
            S -=1
    return ret

if __name__=='__main__':
    try:
        f=open(argv[1])
    except IOError:
        print "No such file: %s" % argv[1]
        exit()
    except IndexError:
        print "No argument was given."
        exit()

    T=int(f.readline())
    for i in xrange(1,T+1):
        line=f.readline()
        l=[int(x) for x in line.split()]
        l.reverse()
        N=l.pop()
        S=l.pop()
        p=l.pop()
        l.reverse()
        print "Case #%d: %d" % (i,maxBest(p,S,l))






