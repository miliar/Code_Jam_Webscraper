T = int(input())
for c in range(T):
  seq, k = input().split(" ")
  k = int(k)
  bitseq =  [{"+":True, "-":False}[e] for e in seq]
    
  def flip(seq, s, l):
    for i in range(s, s+l):
      seq[i] = not seq[i]
    
  count = 0
  for i in range(0, len(bitseq)-k+1):
    if not bitseq[i]:
      flip(bitseq, i, k)
      count += 1
  if not all(bitseq):
    answer = "IMPOSSIBLE"
  else:
    answer = count
  print("Case #{}: {}".format(c+1, answer))
  