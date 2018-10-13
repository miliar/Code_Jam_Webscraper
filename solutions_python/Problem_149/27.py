T = input()
for tc in range(1, T+1):
  N = input()
  A = [int(x) for x in raw_input().split()]
  ct = 0
  while N > 0:
    mn = min(A)
    for i in range(N):
      if A[i] == mn:
        mni = i
    ct += min(mni, N - mni - 1)
    N -= 1
    A = [x for x in A if x != mn]
  print "Case #" + str(tc) + ":", ct