t = int(input())

for ti in range(1,t+1):
  s = list(input())
  while True:
    ok = True
    pre = '0'
    for i in range(len(s)):
      if s[i] < pre:
        s[i-1] = chr(ord(s[i-1])-1)
        for j in range(i,len(s)):
          s[j] = '9'
        ok = False
        break
      pre = s[i]
    if ok: break
  ans = int(''.join(s))
  print('Case #{}: {}'.format(ti,ans))
