T=input()

def intput():
 return map(int,raw_input().split())
def map_input():
 s= []
 global m,n
 for _ in range(n):
  s.append(intput())
 return s
def prt(s):
 print
 for _ in s:
  for __ in _:
   if __ ==1111:
    print 'x',
   else:
    print __,
  print
 print
def ver(index):
 global m,n,s
 return [ s[i][index] for i in range(n)]
 

def cross(i,j):
 global m,n,s,A
 
 a,b,c = set(s[i]) , set(ver(j)) , set(A[:s[i][j]])
 #print s[i][j],a,b,c
 
 if a<=c or b<=c:
  return 0
 return 1
 
def check():
 global m,n,s
 
 
 for i in range(n):
  for j in range(m):
   if cross(i,j):
    return "NO"
 return "YES"

A = range(1,200) 
for _ in range(T):
 nub=0
 n,m = intput()
 s=map_input()
 
 print "Case #"+str(_+1)+":",check()