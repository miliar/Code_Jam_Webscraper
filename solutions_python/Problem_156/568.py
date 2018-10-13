def solve(n,k):
  #if (n == 35 and k == 10):
  #	print memoiz[n][k]
  if (k==0):
    return 0
  if (memoiz[n][k] != -1):
    return memoiz[n][k]
  if n<=k:
    return 0

  #if (n == 35 and k == 10):
  #  print "!!!!",n/k+int(n%k!=0)-1,solve(n/2,k)+solve(n/2+n%2,k)+1
  memoiz[n][k] = min(n/k+int(n%k!=0)-1,solve(n/2,k)+solve(n/2+n%2,k)+1)
  return memoiz[n][k]

memoiz = [-1]*1002
l = []
for i in range(1002):
  l.append(list(memoiz))
memoiz = l
#print len(memoiz),",",len(memoiz[0])
for i in range(1001):
  for j in range(1001):
    solve(i,j)
#print memoiz[31][3]
 
with open('input.txt') as f:
  n= int(f.readline())
  for i in range(n):
    minim = 1000000
    f.readline()
    v = f.readline().split()
    v = [int(x) for x in v]
    m = max(v)

    for j in range(1,m+1):
      total = j
      for x in v:
        total+=solve(x,j)
      minim = min(minim, total)
    print "Case #"+str(i+1)+": ",minim   
   
