

def solve(zi):
  s, k = input().split()
  k = int(k)
  arr = list(c == '+' for c in s)
  n = len(arr)
  ans = 0
  for i in range(n-k+1):
    if not arr[i]:
      ans += 1
      for j in range(i, i + k):
        arr[j] = not arr[j]
  if all(arr):
    print('Case #%d: %d'%(zi+1, ans))
  else:
    print('Case #%d: IMPOSSIBLE'%(zi+1))

zn = int(input())
for zi in range(zn):
  solve(zi)
