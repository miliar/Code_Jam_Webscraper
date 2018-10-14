def solve(s, n):
  p = map(int, s)
  ans = 0
  count = 0
  for i in range(n+1):
    if i <= count: count += p[i]
    else:
      ans += (i - count)
      count += p[i] + (i - count)
  return ans

cases = input()
for caseN in xrange(1, cases+1):
  audi = raw_input().split()
  print("Case #%i: %i" % (caseN, solve(audi[1], int(audi[0]))))


