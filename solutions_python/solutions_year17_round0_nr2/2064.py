import re

def check(N):
  l = len(N)
  if l == 1:
    return N
  else:
    A = N[0]
    a = int(A)
    match = re.search(r'[^{}]'.format(A),N)
    if match:
      idx = match.start()
      if int(N[idx]) < a:
        if a > 1:
          return str(a-1) + '9'*(l-1)
        else:
          return '9'*(l-1)
      else:
        return N[:idx] + check(N[idx:])
    else:
      return N

T = int(input())
for i in range(1,T+1):
  N = input().strip()
  ans = check(N)
  print('Case #{}: {}'.format(i,ans))

