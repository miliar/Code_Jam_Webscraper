f=open("D-large.in","r")
g=open("warlarge.out","w")

T = int(f.readline())

for i in range(0,T):
  N = int(f.readline())
  A = map(float,f.readline().split())
  B = map(float,f.readline().split())
  A.sort()
  B.sort()
  L = []
  while len(A) > 0 or len(B) > 0:
    if len(A) == 0:
      L.append('B')
      B.remove(B[0])
    elif len(B) == 0:
      L.append('A')
      A.remove(A[0])
    else:
      if A[0] < B[0]:
        L.append('A')
        A.remove(A[0])
      else:
        L.append('B')
        B.remove(B[0])

  dwar = 0
  war = N
  countA = 0
  countB = 0
  for l in range(0,len(L)):
    if L[l] == 'B':
      countB += 1
    elif L[l] == 'A' and countB > 0:
      countB -= 1
      dwar += 1
    if L[l] == 'A':
      countA += 1
    elif L[l] == 'B' and countA > 0:
      countA -= 1
      war -= 1

  g.write("Case #"+str(i+1)+": "+str(dwar)+" "+str(war)+"\n")

  
  
  
