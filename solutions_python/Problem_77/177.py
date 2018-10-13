nt = int(input())
for tt in range(nt):
  input()
  a = list(map((lambda x: int(x) - 1), input().split()))
  ans = 0
  for i in range(len(a)):
    if a[i] != i:
      ans += 1
  print('Case #' + str(tt + 1) + ": " + str(ans) + ".000000")
