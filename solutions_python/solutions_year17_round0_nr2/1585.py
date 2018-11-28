import sys

a = []
for line in sys.stdin:
    line = line.strip()
    n = int(line)
    a.append(n)
a = a[1:]

def ans(case, ans):
    print 'Case #' + str(case) + ': ' + str(ans)
    return case + 1

def f(n):
  n = list(str(n))
  d = 0
  for k, v in enumerate(n):
    if int(v) < d:
      n[k-1] = str(int(n[k-1])-1)
      n = [str(9) if (ind >= k) else val for ind,val in enumerate(n)]
      return f(int(''.join(n)))
    d = int(v)
  return ''.join(n)

case = 1
for n in a:
  case = ans(case, f(n))
