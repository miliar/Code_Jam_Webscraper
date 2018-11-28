import sys
T = int(sys.stdin.readline())
for itr in range(T):
  n = list(str(int(sys.stdin.readline())))
  ticki = len(n)
  for i in range(ticki-1,0,-1):
    if n[i]<n[i-1]:
      n[i-1] = chr(ord(n[i-1])-1)
      ticki = i
  print('Case #{}: {}'.format(itr+1, int(
    ''.join(n[0:ticki])+'9'*(len(n)-ticki)
    )))