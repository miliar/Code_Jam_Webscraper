import sys

def main(ifn='ain.txt',ofn='aout.txt'):
    sys.setrecursionlimit(2000)
    with open(ifn) as inf:
        with open(ofn,'w') as ouf:
            noc = int(inf.readline())
            for tnoc in xrange(1,noc+1):
                ouf.write("Case #%d: " %(tnoc))
                print "Case #%d: " %(tnoc)
                n,x = map(int,inf.readline().strip().split(' '))
                s = map(int,inf.readline().strip().split(' '))
                s.sort()
                #print n,x
                #print s
                answer = 0
                while len(s)>0:
                    answer += 1
                    if len(s)==1:
                        s = []
                        continue
                    if s[-1]+s[0]<=x:
                        s = s[1:-1]
                    else:
                        s = s[:-1]
                print "%s" %(answer)
                ouf.write("%s\n" %(answer))

