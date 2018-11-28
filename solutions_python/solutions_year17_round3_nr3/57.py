file_in = open('C-small-1-attempt0.in', 'r')
file_out = open('c.out', 'w')

T = int(file_in.readline())

for t in range(1, T+1):
  print("TEST CASE", t)
  n, k = map(int, file_in.readline().split())
  u = float(file_in.readline())
  p = list(map(float, file_in.readline().split()))
  p.sort(reverse=True)

  added = list(p)
  for i in range(len(p)):
    av = ((sum(p[i:]) + u) / (n-i))
    if av > p[i]:
      added = p[:i] + [av]*(n-i)
      break

  print(added)

  prod = 1
  for probability in added:
    prod *= probability

  ans = prod

  if ans > 1:
    ans = 1
  file_out.write("Case #{0}: {1:10f}\n".format(t, ans))