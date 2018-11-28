
def main(ifn='ain.txt',ofn='aout.txt'):
    with open(ifn) as inf:
        with open(ofn,'w') as ouf:
            noc = int(inf.readline().strip())
            for tnoc in xrange(noc):
                ouf.write("Case #%d: " %(tnoc+1))
                d = dict()
                r = int(inf.readline().strip())
                for i in xrange(4):
                    l = map(int,inf.readline().strip().split(' '))
                    if r-1==i:
                        for x in l:
                            v = d.get(x,0)
                            d[x] = v+1
                r = int(inf.readline().strip())
                for i in xrange(4):
                    l = map(int,inf.readline().strip().split(' '))
                    if r-1==i:
                        for x in l:
                            v = d.get(x,0)
                            d[x] = v+1
                c = [k for k,v in d.items() if v==2]
                if 0==len(c):
                    ouf.write("Volunteer cheated!\n")
                elif 1==len(c):
                    ouf.write("%d\n" %(c[0]))
                else:
                    ouf.write("Bad magician!\n")
