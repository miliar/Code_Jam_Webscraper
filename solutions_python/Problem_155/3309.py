T = input()
S = []
Out = []
for i in range(T):
  S.append(raw_input().split()[1])
# print S
for st in S:
  pop = 0
  need = 0
  for i in range(len(st)):
    num = int(st[i])
    curNeed = max(i - pop, 0)
    pop = pop + num + curNeed
    need += curNeed
  Out.append(need)
for i in range(T):
  output = "Case #%d: %d" % (i + 1, Out[i])
  print output