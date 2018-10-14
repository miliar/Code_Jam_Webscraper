#!/usr/bin/env python
vowels="aiueo"
consonants="bcdfghjklmnpqrstvwxyz"
def solve(L, n):
    ans=[]
    ns=[x for x in range(n,len(L)+1)]
    for nx in ns:
        for i in range(len(L)-nx+1):
            x=L[i:i+nx]
            c=0
            for xx in x:
                if xx in vowels: c=0
                else: c+=1
                if c>=n:
                    ans.append(x)
                    break

    return len(ans)

if __name__=='__main__':
    N=int(raw_input())
    for x in range(1,N+1):
        L,n=map(str,raw_input().split())
        print 'Case #%d: %d'% (x,solve(L,int(n)))

