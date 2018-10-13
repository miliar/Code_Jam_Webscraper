#!/usr/bin/env python2.6

def main(fin,fout):
    iter = int(fin.readline())
    for i in range(iter):
        rkn = map(int,fin.readline().split(" "))
        k = rkn[1]
        r = rkn[0]
        grps = map(int,fin.readline().split(" "))
        tgrps = grps
        q = 0
        total = 0
        for ri in range(r):
            q = 0
            pops = 0
            tgrps = grps[:]
            while 1:
                t1 = tgrps.pop(0)
                t2 = q + t1
                if t2 <= k:
                    q += t1
                    total += t1
                    pops += 1
                else:
                    break
                if len(tgrps)==0:
                    break
            for pop in range(pops):
                x = grps.pop(0)
                grps.append(x)
        fout.write("Case #%d: %d\n" % (i+1,total))
                
                
                
        #fout.write(str)

if __name__ == "__main__":
    with open("C-small-attempt0.in","r") as fin:
        with open("csmall.out","w") as fout:
            main(fin,fout)
    print "done"
