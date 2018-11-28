char1="abcdefghijklmnopqrstuvwxyz "
char2="ynficwlbkuomxsevzpdrjgthaq "

def ints():
  return map(int, raw_input().split())

num_cases, = ints()

for case_num in xrange(1, num_cases + 1):
  G = raw_input()

  G = [char1[char2.find(c)] for c in G]
  
  print "Case #%d: %s" % (case_num, ''.join(G))

