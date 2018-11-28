import sys

def buys(C,F,X,n):
  return sum(C/(2.0+i*F) for i in range(n)) + X/(F*n + 2)

for case in range(int(sys.stdin.readline())):
  C, F, X = map(float, sys.stdin.readline().strip().split(' '))

  ans = buys(C, F, X, 0)
  i = 1
  while True:
    n = buys(C, F, X, i)
    if n < ans:
      ans = n
    else:
      break
    i += 1

  print "Case #" + str(case+1) + ": " + str(ans)
