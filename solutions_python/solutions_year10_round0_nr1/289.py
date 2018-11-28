#!/usr/bin/env python2.6

def main(fin,fout):
    iter = int(fin.readline())
    for i in range(iter):
        nk = fin.readline().split(" ")
        n = int(nk[0])
        k = int(nk[1])
        if k == 0:
            fout.write("Case #%d: OFF\n" % (i+1))
        else:
            nsq = pow(2,n)
            rem = k % nsq
            nsqs = nsq - 1
            if rem == nsqs:
                fout.write("Case #%d: ON\n" % (i+1))
            else:
                fout.write("Case #%d: OFF\n" % (i+1))
if __name__ == "__main__":
    with open("A-large.in","r") as fin:
        with open("al.out","w") as fout:
            main(fin,fout)
    print "done"
