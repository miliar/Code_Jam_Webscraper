T = int(input())
def istidy(N):
  n=str(N)
  return all([n[i]<= n[i+1] for i in range(len(n)-1)])
for i in range(1, T + 1):
  N = int(input())
  while not istidy(N): N-=1
  print("Case #{}: {}".format(i, N))