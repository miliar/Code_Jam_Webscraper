# python3
T = int(input())
for t in range(1, T + 1):
  N, X = map(int, input().split())
  S = list(map(int, input().split()))
  S.sort()
  L, R = 0, len(S) - 1
  ans = 0
  while L <= R:
    if L == R:
      ans += 1
      L += 1
    else:
      ans += 1
      if S[L] + S[R] <= X:
        L += 1
      R -= 1
  print("Case #{}: {}".format(t, ans))

