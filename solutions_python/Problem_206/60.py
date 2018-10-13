T = int(input())

# def solve():

for i in range(1,T+1):
  D, N = map(int, input().split(' '))
  v = 0
  for j in range(N):
    K, S = map(int, input().split(' '))
    v = max((D-K)/S, v)
  print("Case #{}: {}".format(i, D/v))