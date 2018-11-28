import sys

t = int(raw_input())

for i in xrange(1, t+1):
  r, c = raw_input().strip().split()
  r = int(r)
  c = int(c)
  cake = []
  for j in xrange(r):
    cakerow = list(raw_input().strip())
    cake.append(cakerow)


  for m in xrange(r):
    n = 0
    while n < c:
      if cake[m][n] != "?":
        l , h = n-1, n+1
        while l >= 0 and cake[m][l] == "?":
          cake[m][l] = cake[m][n]
          l -= 1
        while h < c and cake[m][h] == "?":
          cake[m][h] = cake[m][n]
          h += 1
      n += 1
    if cake[m][0] == "?":
      if m > 0: 
        cake[m] = cake[m-1]
        
  ll = 0
  while ll < r and cake[ll][0] == "?":
    ll += 1
  
  ll -= 1
  while ll >= 0 and cake[ll][0] == "?":
    cake[ll] = cake[ll + 1]
    ll -= 1

  
  print "Case #{}: ".format(i)
  for line in cake:
    s = ''.join(line)
    print s