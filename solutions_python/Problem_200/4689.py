def not_tidy(n):
  s = str(n)
  return not (len(s) == 1 or all(s[i] <= s[i+1] for i in range(len(s)-1)))

T = int(input())
for i in range(1, T+1):
  N = int(input())
  while not_tidy(N):
    N -= 1
  print("Case #{}: {}".format(i, N))