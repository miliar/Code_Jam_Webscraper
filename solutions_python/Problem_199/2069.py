for t in range(1,input()+1):
  s, k = raw_input().split()
  s = bytearray(s)
  k = int(k)
  ans = 0
  for i in range(len(s)-k+1):
    if chr(s[i]) == '+': continue
    ans += 1
    for j in range(k):
      s[i+j] = {'+':'-','-':'+'}[chr(s[i+j])]
  for x in s[-k:]:
    if chr(x) != '+':
      ans = 'IMPOSSIBLE'
  print 'Case #%i:'%t, ans
