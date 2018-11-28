def getlist(n):
  l=[]
  while n>0:
    l.append(n%10)
    n//=10
  l.reverse()
  return l

def getrevlist(n):
    l=getlist(n)
    t=[]
    L=len(l)
    for i in range(0,L):
        t.append(l[L-i-1])
    return tdef IsPalindrome(n):
    if getlist(n)==getrevlist(n):
        return 1
    else:
        return 0

def IsPalindrome(n):
    if getlist(n)==getrevlist(n):
        return 1
    else:
        return 0
import numpy
	
def Count(A,B):
    count=0
    a=numpy.int64(sqrt(A))
    b=numpy.int64(sqrt(B))
    for i in range(a, b+1):
        if i in l:
            C=i*i
            if IsPalindrome(C):
                if C<A:
                    pass
                elif C>B:
                    pass                        
                else:
                    print C
                    count+=1        
    return count       

fin=open('/home/nikhil/Downloads/C-small-attempt0.in','rt')
fout=open('/home/nikhil/Desktop/output.txt','wt')
s=fin.readline()
num=int(str.split(s,'\n')[0])
for a in range(num):
    s=fin.readline()
    k=str.split(s,' ')
    A=int(k[0])
    B=int(k[1])
    fout.write('Case #%d: %d\n'%(a+1,Count(A,B)))
fout.close()
l=[]
for i in range(1,10000001):
    if IsPalindrome(i)==1:
        l.append(i)
