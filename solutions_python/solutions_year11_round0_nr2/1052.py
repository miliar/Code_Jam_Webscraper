#!/usr/bin/python
#Eugeny Zagumennov, aciddd87@mail.ru
import sys
com, opp = [], []
def iscom(c1, c2):
    global com
    if c1==c2: 
        for i in range(len(com)):
            if (c1+c2) == com[i]: 
                return i
    else:
        for i in range(len(com)):
            if (c1 in com[i]) and (c2 in com[i]):
                return i
    return -1
def isopp(l,c2):
    global opp
    for i in range(len(opp)):
        if c2 in opp[i]:
            if c2==opp[i][0]: c=opp[i][1]
            else: c=opp[i][0]
            for el in l:
                if c in l:
                    return 1
    return -1
def main():
    global com, opp
    fin=open(sys.argv[1], "r")
    fout=open("OUTPUT.txt", "w")
    T=int(fin.readline().strip())
    for t in range(T):
        l=fin.readline().strip().split()
        comTo = []
        com, opp = [], []
        s=l[-1]
        C=int(l[0])
        D=int(l[1+C])
        N=int(l[2+C+D])
        if C!=0:
            for i in range(C):
                com.append(l[1+i][:2])
                comTo.append(l[1+i][2])
        if D!=0:
            for i in range(D):
                opp.append(l[2+C+i][0:2])
        l=[]
        if C==D==0: 
            res="Case #%i: ["%(t+1)
            for i in range(len(s)-1):
                res+=s[i]+", "
            res+=s[-1]+"]\n"
            fout.write(res)
        else:
            for i in range(0, len(s)):
                if l==[]:
                    l.append(s[i])
                    continue
                j=iscom(l[-1], s[i])
                k=isopp(l, s[i])
                if j!=-1:
                    l[-1]=comTo[j]
                elif k!=-1:
                    l=[]
                else: l.append(s[i])
            res="Case #%i: ["%(t+1)
            for i in range(len(l)-1):
                res+=l[i]+", "
            if len(l)>0: res+=l[-1]+"]\n"
            else: res+="]\n"
            fout.write(res)
    fin.close()
    fout.close()    
if __name__=="__main__":
    main()