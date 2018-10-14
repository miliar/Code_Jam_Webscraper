from sys import stdin

T = int(stdin.readline())

# grouping together GK[i], looking at adding GK[j]
def CB(i, j, w, m, G, GK, H, I, S):
  r = CB2(i, j, w, m, G, GK, H, I, S)
  return r

def CB2(i, j, w, m, G, GK, H, I, S):
  if j >= len(GK):
    if i == j:
      return 0
    else:
      return float("inf")
  g = GK[i]
  if i == j:
    if g in S:
      return CB(i+1, i+1, 0, 0, G, GK, H, I, S)
    else:
      return CB(i, i+1, len(I[g]), len(H[g]), G, GK, H, I, S)
  L = CB(i, j+1, w, m, G, GK, H, I, S)
  h = GK[j]
  if h in S:
    return L
  U = w * len(H[h]) + m * len(I[h])
  w += len(I[h])
  m += len(H[h])
  S.add(h)
  if w == m:
    U += CB(i+1, i+1, 0, 0, G, GK, H, I, S)
  else:
    U += CB(i, j+1, w, m, G, GK, H, I, S)
  S.remove(h)
  return min(L, U)
  
def run():
  for t in range(T):
    N = int(stdin.readline())
    A = []
    for _ in range(N):
      A.append(stdin.readline())

    G = {}
    H = {}
    I = {}
    for n in range(N):
      if n in G:
        continue
      S = [n]
      G[n] = n
      H[n] = [n]
      I[n] = set()
      while S:
        s = S.pop()
        for m in range(N):
          if A[m][s] == '1':
            if not m in I[n]:
              I[n].add(m)
              for o in range(N):
                if A[m][o] == '1' and o not in G:
                  G[o] = n
                  H[n].append(o)
                  S.append(o)
    M = N
    for n in range(N):
      if n not in G:
        I[M] = set()
        H[M] = [n]
        M += 1
    for a in range(len(A)):
      if not any(c == '1' for c in A[a]):
        I[M] = set([a])
        H[M] = []
        M += 1

    C = sum([len(H[h]) * len(I[h]) - sum(1 if c == '1' else 0 for c in "".join(A[i] for i in I[h])) for h in H])
    GK = list(H.keys())
    S = set(g for g in GK if len(H[g]) == len(I[g]))
    print("Case #{}: {}".format(t +1,  C + CB(0, 0, 0, 0, G, GK, H, I, S)))

run()
