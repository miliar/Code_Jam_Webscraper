#!c:\Python33\python.exe
# vim:fileencoding=utf-8

import sys
import re
import glob
import itertools
import pdb


def in_out():
    infiles = glob.glob("*.in")
    for infile in infiles:
        keyword = (sys.argv[1] if len(sys.argv)>1 else "test")
        if re.search(keyword, infile):
            return (open(infile,"r"), open(infile[:-2]+"out", "w+"))

def main():
    fin,fout = in_out()
    casenum = int(fin.readline()[:-1])
    for i in range(casenum):
        N,M=fin.readline()[:-1].split()
        N=int(N)
        M=int(M)
        #print(N,M)
        a=[]
        for j in range(N):
            a.append(fin.readline()[:-1].split())
        #print(a)
        res="YES"
        for n in range(N):
            for m in range(M):
                impossible=0
                h=a[n][m]
                for j in range(N):
                    if a[j][m]>h:
                        impossible+=1
                        break
                if impossible==0:
                    continue
                for j in range(M):
                    if a[n][j]>h:
                        impossible+=1
                        break
                if impossible==2:
                    res="NO"
                    break
            if res=="NO":
                break
        fout.write('Case #'+str(i+1)+": "+res+"\n")

    fout.flush()
    fout.seek(0)
    print(fout.read())

if __name__ == "__main__":
    main()

