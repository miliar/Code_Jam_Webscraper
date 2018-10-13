def bcount(L1, L2):
  i1, i2 = 0, 0
  result = 0
  while i1 < len(L1) and i2 < len(L2):
    if L1[i1] > L2[i2]:
      i1 += 1
      i2 += 1
      result += 1
    else:
      i2 += 1
  return result


T = int(input())
for t in range(1, T + 1):
  N = int(input())
  A = list(map(float, input().split()))
  B = list(map(float, input().split()))
  A.sort(reverse=True)
  B.sort(reverse=True)
  print("Case #{}: {} {}".format(t, bcount(A, B), N - bcount(B, A)))
