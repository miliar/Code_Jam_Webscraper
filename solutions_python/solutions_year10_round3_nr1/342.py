#!/usr/bin/env python2.6

def main(fin,fout):
    iter = int(fin.readline())
    for i in range(iter):
        n = int(fin.readline())
        p = {}
        for ni in range(n):
            tmp = map(int, fin.readline().split(' '))
            p[tmp[0]] = tmp[1]
        ht = 0
        isect = 0
        for ni in p:
            if p[ni] > ht:
                ht = p[ni]
                for nj in p:
                    if nj > ni:
                        ht2 = p[nj]
                        if ht2 < ht:
                            isect += 1
        fout.write('Case #%d: %d\n' % (i+1,isect))
        #fout.write(str)
if __name__ == "__main__":
    with open("A-small-attempt0.in","r") as fin:
        with open("as.out","w") as fout:
            main(fin,fout)
    print "done"
