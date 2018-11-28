import sys

def cp(s0,s1):
    l0 = len(s0)
    l1 = len(s1)
    l = min(l0,l1)
    for i in xrange(l):
        if s0[i]!=s1[i]:
            return i
    return l

def main(ifn='din.txt',ofn='dout.txt'):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn,'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1,noc+1):
                ouf.write("Case #%d: " %(tnoc))
                print "Case #%d: " %(tnoc)
                m,n = map(int,inf.readline().strip().split(' '))
                s = []
                for i in xrange(m):
                    s.append(inf.readline().strip())
                total = n**m
                answer = 0
                count = 0
                for i in xrange(total):
                    r = []
                    tmp = i
                    for j in xrange(m):
                        r.append(tmp%n)
                        tmp /= n
                    empty = False
                    tanswer = 0
                    for j in xrange(n):
                        sj = [s[x] for x in xrange(m) if r[x]==j]
                        if len(sj)==0:
                            empty = True
                            break
                        sj.sort()
                        vv = 1+len(sj[0])
                        l = len(sj)
                        for k in xrange(1,l):
                            p = cp(sj[k-1],sj[k])
                            vv += len(sj[k])-p
                        tanswer += vv
                        #print sj,vv
                    if empty:
                        continue
                    #print r,tanswer
                    if tanswer>answer:
                        answer = tanswer
                        count = 1
                    elif tanswer==answer:
                        count += 1
                ouf.write("%d %d\n" %(answer,count))
                print "%d %d" %(answer,count)

