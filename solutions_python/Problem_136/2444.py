
def main(ifn='bin.txt',ofn='bout.txt'):
    with open(ifn) as inf:
        with open(ofn,'w') as ouf:
            noc = int(inf.readline().strip())
            for tnoc in xrange(noc):
                ouf.write("Case #%d: " %(tnoc+1))
                c,f,x = map(float,inf.readline().strip().split(' '))
                print c,f,x
                bestanswer = x
                t = 0.0
                p = 2.0
                while True:
                    tmpanswer = t+x/p
                    if tmpanswer<bestanswer:
                        bestanswer = tmpanswer
                    if t>bestanswer:
                        break
                    t += c/p
                    p += f
                ouf.write("%.10lf\n" %(bestanswer))
                print bestanswer
