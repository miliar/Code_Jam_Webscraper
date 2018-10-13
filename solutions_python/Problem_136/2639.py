import math

T = int(input())

def time_to_win(nfactories, C, F, X):
  time = 0
  for i in range(nfactories):
    time += C / (2.0 + i*F)

  return time + (X / (2.0 + nfactories*F))

for t in range(1, T+1):
  C, F, X = map(float, input().split(" "))

  inc = int(math.sqrt(X))

  mint = time_to_win(0, C, F, X)
  minn = 0
  for n in range(1,int(X),inc):
    time = time_to_win(n, C, F, X)
    if time > mint:
      break
    mint = time
    minn = n
  
  mint = min([time_to_win(i, C, F, X) for i in range(max(0, minn-inc), minn+inc+1)])

  print("Case #%i:" % t, mint)
