N = int(input())
for i in range(N):
  a = int(input()) - 1
  A = [list(map(int, input().split())) for j in range(4)]
  b = int(input()) - 1
  B = [list(map(int, input().split())) for j in range(4)]
  s = set(A[a]).intersection(set(B[b]))
  if len(s) == 0:
    print("Case #%d: Volunteer cheated!" % (i + 1))
  elif len(s) == 1:
    print("Case #%d: %d" % (i + 1, s.pop()))
  else:
    print("Case #%d: Bad magician!" % (i + 1))
