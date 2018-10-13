te = int(input())
for t in range(1, te + 1):
  ans = 0
  cnt = 0
  inp = input().split()
  n = int(inp[0])
  for i in range(0, len(inp[1])):
    x = int(inp[1][i])
    if cnt < i:
      ans += i - cnt
      cnt += i - cnt
    cnt += x
  print ("Case #%i: %i" % (t, ans))
