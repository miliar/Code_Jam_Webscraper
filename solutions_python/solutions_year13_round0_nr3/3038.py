from math import sqrt

def is_fair(beta):
  if beta < 10:
    return True
  beta = str(beta)
  n = len(beta)
  c = n // 2
  for i in xrange(c):
    x = n - 1 - i
    if beta[x] is not beta[i]:
      return False
  return True

def is_sqaure(gamma):
  return gamma % sqrt(gamma) == 0
  

def is_fair_and_sqaure(delta):
  return is_sqaure(delta) and is_fair(delta) and is_fair(int(sqrt(delta)))


in_file="C-small-attempt0.in"
out_file="out.txt"
t = 0
cases = []
results = []
with open(in_file) as f:
  t = int(f.readline())
  for i in xrange(t):
    raw = f.readline()
    alpha = tuple(map(int, raw.split()))
    cases.append(alpha)


for a, b in cases:
  fas = [1 for i in xrange(a, b+1) if is_fair_and_sqaure(i)]
  results.append(sum(fas))


with open(out_file, 'w+') as f:
  for i, r in enumerate(results):
    f.write("Case #%s: %s" % (i + 1, r))
    if i != len(cases) -1:
      f.write("\n")
