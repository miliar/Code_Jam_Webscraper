import io, os, sys

data = open(sys.argv[1]).readlines()

T = int(data[0])

count = 0
num = 1
while count < T:
  count += 1
  A = data[num]
  num += 1
  n,k = int(A.split(" ")[0]), int(A.split(" ")[1])
  print 'n',n,'k',k
  R = []
  tmp = 0
  while tmp < n:
    tmp += 1
    A = data[num].split(" ")
    print A
    R.append([int(A[0]), int(A[1]), int(A[0])*int(A[1])])
    num += 1
    print tmp, n
  R.sort(reverse=True)
  print R
  ans = []
  tmp = 0
  while tmp < n-k+1:
    a = R[tmp][0]*R[tmp][0] + 2*R[tmp][2]
    r = R[tmp+1:]
    print tmp, a, r
    r.sort(reverse=True,key=lambda x:x[2])
    for i in range(k-1):
      a += 2*r[i][2]
    a *= 3.14159265358979
    ans.append(a)
    tmp += 1
  ans.sort()
  print ans
  print 'Case #' + str(count) + ': ' + str(ans[-1])

    
  
