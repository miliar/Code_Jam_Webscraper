import sys,re
import string

def ri(f):  
    return int(f.readline().strip())
def rlf(f,fn):
    return map(fn, f.readline().strip().split())

def rl(f):
    return f.readline().strip().split()

def swap(a,x,y):
    a[x] = (a[x], a[y])
    a[y] = a[x][0]
    a[x] = a[x][1]

def bad(s,n):
    #print s +" " + str(n)
    for i in range(n+1,len(s)):
        if s[i]=='1':
            #print s + " " + str(i)
            return True
            
    return False


f=open( sys.argv[1])
N=ri(f)
for i in xrange(N):
    n=ri(f)
    L=[]
    for j in range(n):
        L.append((f.readline().strip()))
    complete = True
    rval=0
    while True:
        for j in range(n):
            if bad(L[j],j):
                for k in range(j+1,n):
                    if not bad(L[k],j):
                        xx = L.pop(k)
                        L.insert(j,xx)
                        rval+=k-j
                        complete = False
                        break
                break        
        if complete: break
        complete = True

    print "Case #"+str(i+1)+": "+ str(rval) 


