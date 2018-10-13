def Filp(S, K, p):
    for i in range(p,p+K):
        if S[i] == "+":
            S[i] = "-"
        elif S[i] == "-":
            S[i] = "+"
    return S
    
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  for s in input().split(" "):
    if "+" in s or "-" in s:
      S = list(s)
    else:
      K = int(s)
  N = len(S)
  count = 0
  
  for j in range(0,N-K+1):
    if S[j] == "-":
        Filp(S,K,j)
        count = count + 1
  result = count
  for j in range(N-K+1,N):
    if S[j] == "-":
        result = "IMPOSSIBLE"
        break
 
  print("Case #{}: {}".format(i, result))