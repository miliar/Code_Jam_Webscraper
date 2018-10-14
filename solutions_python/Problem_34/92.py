
def main(inp):
  L, D, N = (int(x) for x in inp.readline().split(' '))
  tree = dict()
  for i in xrange(D):
    word = inp.readline().strip()
    curr = tree
    for c in word:
      if c not in curr:
        curr[c] = dict()
      curr = curr[c]
  for i in xrange(1, N+1):
    word = inp.readline().strip()
    comps = parse(word)
    count = all(comps, tree)
    print "Case #%s: %s" % (i, count)

def parse(word):
  comps = []
  prev = -1
  for i, c in enumerate(word):
    if c == ')':
      comps.append(word[prev+1:i])
      prev = -1
    elif c == '(':
      prev = i
    elif prev == -1:
      comps.append(c)
  return comps

def all(comps, tree, i=0):
  if i == len(comps):
    return 1
  res = 0
  for c in comps[i]:
    if c in tree:
      res += all(comps, tree[c], i+1)
  return res

if __name__ == "__main__":
  import sys
  main(sys.stdin)
