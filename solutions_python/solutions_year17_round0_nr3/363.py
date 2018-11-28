

testnum = int(input())
for i in range(1, testnum+1):
  N, K = [int(x) for x in input().split(" ")]
  while K>1:
    if K%2:
      N = (N-1)//2
    else:
      N = (N-1)//2+(N-1)%2
    K = K//2
  LS = (N-1)//2
  RS = (N-1)//2+(N-1)%2
  print(max(LS,RS), min(LS,RS))