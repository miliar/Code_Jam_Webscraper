for t in range(1,input()+1):
  n, k = map(int, raw_input().split())
  a = [n]
  for i in range(k):
    idx = 0
    for j in range(len(a)):
      if a[j] > a[idx]: idx = j
    temp = a[idx]
    left = (temp-1)/2
    rite = temp/2
    a[idx:idx+1] = [left, rite]
  print 'Case #%i:'%t, rite, left
