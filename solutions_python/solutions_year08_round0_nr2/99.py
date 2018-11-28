import sys

N=int(input())
for step in range(N):
  T=int(input())
  na,nb=map(int,raw_input().split())
  A=[]
  B=[]
  for i in range(na+nb):
    s=raw_input().split()
    leaving = 60*int(s[0][:2])+int(s[0][3:5])
    arriving = 60*int(s[1][:2])+int(s[1][3:5])
    if i<na:
      A.append((leaving,arriving))
    else:
      B.append((leaving,arriving))
    AA = []
    for t in A:
      AA.append((t[0],1))
    for t in B:
      AA.append((t[1]+T,-1))
    AA.sort()
    a=0
    count=0
    for t,c in AA:
      count += c
      a = max(count,a)
    BB = []
    for t in B:
      BB.append((t[0],1))
    for t in A:
      BB.append((t[1]+T,-1))
    BB.sort()
    b=0
    count=0
    for t,c in BB:
      count += c
      b = max(count,b)

  
  sys.stderr.write(str(step+1)+' ')
  print 'Case #%s: %s %s'%(step+1,a,b)

sys.stderr.write('\n')
