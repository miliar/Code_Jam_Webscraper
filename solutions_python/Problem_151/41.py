def ints():
  return [int(x.strip()) for x in raw_input().split(' ')]
cases = input()


def maketrie():
  return {}

def counttrie(trie):
  if len(trie) == 0:
    return 1
  return 1 + sum(counttrie(t) for t in trie.itervalues())

def addtrie(trie, s):
  for c in s:
    if c not in trie:
      trie[c] = maketrie()
    trie = trie[c]

for casenum in range(1, cases+1):
  m,n=ints()
  s = []
  for i in range(m):
    s.append(raw_input())


  triecounts = []
  for k in range(n**m):
    bits = []
    for _ in range(m):
      bits.append(k%n)
      k/=n
    tries = [maketrie() for _ in range(n)]
    for i in range(m):
      addtrie(tries[bits[i]], s[i])
    triecounts.append(sum(0 if len(trie)==0 else counttrie(trie) for trie in tries))
  #print triecounts
  m = max(triecounts)
  c = len([x for x in triecounts if x==m])
  print "Case #" + str(casenum) + ": ", m, c