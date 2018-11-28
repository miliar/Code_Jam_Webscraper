#!/usr/bin/python
#Eugeny Zagumennov, aciddd87@mail.ru
import sys
def sum(n1, n2):
    n=len(bin(max(n1,n2)))-1
    s=""
    for i in range(1,n):
        if (n1%(1<<i)/(1<<(i-1))) == (n2%(1<<i)/(1<<(i-1))) : s="0"+s
        else: s="1"+s
    return int("0b"+s,2)
def sumL(l):
    res=0
    for i in range(len(l)):
        res=sum(res, l[i])
    return res
def main():
    fin=open(sys.argv[1], "r")
    fout=open("OUTPUT.txt", "w")
    T=int(fin.readline().strip())
    for test in range(T):
        N=int(fin.readline().strip())
        l=fin.readline().strip().split()
        L=[int(x) for x in l]
        del l
        L.sort()
        res=0
        for i in range(0, N):
          if res!=0: break
          for j in range(i+1, N):
            s1, s2 = sumL(L[0:i+1]), sumL(L[i+1:])
            if s1==s2: 
                for k in range(j, N): res+=L[k]
                break
            t=L.pop(j)
            L.insert(i, t)
            l=L[i+1:]
            l.sort()
            L=L[0:i+1]+l
        if res==0: res="NO"
        fout.write("Case #%i: %s\n"%(test+1, res))
    fin.close()
    fout.close()    
if __name__=="__main__":
    main()