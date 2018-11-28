#!/usr/bin python

def wip(sch,x):
    x = [float(i) for i in x if (i != '.')]
    if len(x) > 0:
        return sum(x)/len(x)
    return 0

def owip(sch,team):
    mtrx = []
    for i,x in enumerate(sch[team]):
        if x == '.':
            continue
        else:
            a = sch[int(i)]
            #print "hallo",a[0:team]+a[team+1:]
            mtrx.append(a[0:team]+a[team+1:])

    #print 'matrix', mtrx
    tmp = [wip(mtrx,i) for i in mtrx]
    if len(tmp) > 0:
        return sum(tmp)/len(tmp)
    return 0

def oowip(sch,owp,team):
    mtrx = []
    for i,x in enumerate(sch[team]):
        if x == '.':
            continue
        else:
            mtrx.append(owp[i])
    #print 'oopwmatrix',mtrx
    if len(mtrx) > 0:
        return sum(mtrx)/len(mtrx)
    return 0 


def main():
    path = "A-large.in"
    f = open(path)
    T = int(f.readline())
    for C in range(1,T+1):
        sch = []
        wp = []
        owp = []
        oowp = []
        N = int(f.readline())
        for x in range(N):
            s = f.readline()
            #print 'add', x, s
            s = s.strip()
            sch.append([c for c in s])

        #print "schedule",sch
        for x in range(N):
            wp.append(wip(sch,sch[x]))
            owp.append(owip(sch,x))

        for x in range(N):
            oowp.append(oowip(sch,owp,x))

        #print wp, owp, oowp

        print "Case #"+str(C)+":"
        for x in range(N):
            print 0.25*wp[x]+0.5*owp[x]+0.25*oowp[x]

if __name__ == "__main__":
    main()
