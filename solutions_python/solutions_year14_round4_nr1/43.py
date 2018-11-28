from sys import stdin

T = int(stdin.readline())

for case_no in range(1, T+1):
  N, X = map(int, stdin.readline().split())
  S = map(int, stdin.readline().split())
  S.sort()

  ans = 0
  last = 0
  while len(S) > last:
    if len(S) == last:
      ans += 1
      break
    if S[-1] + S[last] <= X:
      ans += 1
      last += 1
      S.pop()
    else:
      S.pop()
      ans += 1
  print "Case #%d: %d" % (case_no, ans)
