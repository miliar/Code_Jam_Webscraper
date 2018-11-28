concat = lambda a, b: a + b if a > '0' else b
tidy = lambda n: len(n) <= 1 or (n[0] <= n[1] and tidy(n[1:]))
solve = lambda n: n if tidy(n) else concat(solve(str(int(n)//10-1)), '9')

t = int(input())
for i in range(1, t+1):
  print("Case #%s: %s" % (i, solve(input())))
