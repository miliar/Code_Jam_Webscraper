'''
Created on 12/04/2014

@author: david
'''
from itertools import groupby

#f=open("exampleB.txt")
f=open("B-small-attempt4.in")
#f=open("B-large.in")

T=int(f.readline())
P=[]
for i in range(T):
    f.readline()
    p = [int(n) for n in f.readline().split()]
    P.append(p)


def solve(p):
    def rec(d, l):
        #print(" "*l+"--len(d)", len(d))
        if len(d)==0:
            return 0
        kkk = list(d.keys())
        kkk.sort(reverse=True)
        n = kkk[0]
        n2 = kkk[1] if len(kkk)>1 else int(10e50)
        #print(" "*l+"--n", n)
        if n<=3:
            return n
        jj = list(d.items())
        jj.sort()
        jj = tuple(jj)
        if jj not in mem:
            """
            d2 = {}
            for k,v in d.items():
                if k==n:
                    if v>1:
                        d2[n] = v-1
                    p1 = n//2
                    p2 = n-p1
                    d2.setdefault(p1,0)
                    d2.setdefault(p2,0)
                    d2[p1] += 1
                    d2[p2] += 1
                else:
                    d2.setdefault(k,0)
                    d2[k] += v
            s2 = rec(d2, l+1)
            """
            s2 = float('inf')
            ##if n2<n//2:
            for nnn in range(1,n//2+1):
                d2b = {}
                for k,v in d.items():
                    if k==n:
                        if v>1:
                            d2b[n] = v-1
                        p1 = nnn                      
                        p2 = n-p1
                        d2b.setdefault(p1,0)
                        d2b.setdefault(p2,0)
                        d2b[p1] += 1
                        d2b[p2] += 1
                    else:
                        d2b.setdefault(k,0)
                        d2b[k] += v
                s2b = rec(d2b, l+1)
                s2 = min(s2,s2b)
                    
            d3 = {}
            for k,v in d.items():
                if k>1:
                    d3[k-1] = v
            s3 = rec(d3, l+1)
            
            #print(" "*l+"--d2", d2)
            #print(" "*l+"--s2", s2)
            #print(" "*l+"--d3", d3)       
            #print(" "*l+"--s3", s3) 
            mem[jj] = min(s2, s3) + 1
            #print(" --rr", RR)
        return mem[jj]
    
    p.sort()
    d = {}
    for key, group in groupby(p, lambda x: x): 
        d[key] = len(list(group))
    #print(p,d)
    mem = {}
    return rec(d, 0)

def solve2(p):
    s = 0
    p.sort(reverse=True)
    while len(p)>0: 
        s+=1 
        m = p[0]
        num = 1
        #while num<len(p) and p[num]==m:
        #    num+=1
        num = p.count(m)
        o = opt(m)
        
        if o+num-1<m:
            del p[0]
            p.append(m//2)
            p.append(m-m//2)
            p.sort(reverse=True)
        else:
            p2 = [v-1 for v in p if v>1]
            p = p2
    return s
       
#for n in range(2,10):
#    print(2**n+2, opt(2**n+2))
    
fRes = open("res.txt", "w")
case=0
ss=0
for p in P:
    print(p)
    #if case==10: break
    case+=1
    sol = solve(p)
    ss+=sol
    print("Case #{}: {}".format(case,sol))
    fRes.write("Case #{}: {}\n".format(case,sol))
print(ss)
        
fRes.close()