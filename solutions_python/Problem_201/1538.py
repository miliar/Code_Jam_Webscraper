def toilet(N, K):
  s=1
  while N-s>0 and s<K:
    N=N-s
    K=K-s
    s=s*2
  t=N//s
  if (t+1)*K+(s-K)*t<=N and s*t<N:
    t=t+1
  if t%2==1:
    max=(t-1)/2
    min=(t-1)/2
  else:
    max=t/2
    min=t/2-1
  return [int(max), int(min)]
  

T = int(input())  # read a line with a single integer
N=[0]*T
K=[0]*T

for i in range(0, T ):
  N[i], K[i] = [int(s) for s in input().split(" ")]

for i in range(0, T ):
  ans=toilet(N[i], K[i])
  print("Case #{}: {} {}".format(i+1, ans[0], ans[1]))
