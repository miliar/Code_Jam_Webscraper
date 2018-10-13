from copy import copy
cases = xrange(int(raw_input()))
a = {'size' : 0}
size = 0
string = ""
groups = []

def calc_group(group, previous, perm):
  retcount = 0
  prev = previous
  for p in perm:
    cur = group[p - 1]
    if cur != prev:
      retcount += 1
    prev = cur
  return (retcount, prev)
    
def calc(perm):
  prev = 'A'
  count = 0
  for group in groups:
    new_count, prev = calc_group(group, prev, perm)
    count += new_count
    if count >= a['size']:
      return
  a['size'] =  count
  

def xxx(perm_seq, rest):
  if len(rest) == 0:
    calc(perm_seq)
  else:
    for x in range(len(rest)):
      new_rest = [z for z in rest]
      new_x = rest[x]
      new_rest.remove(new_x)
      xxx(perm_seq + [new_x], new_rest)
      
for case in cases:
  groupsize = int(raw_input())
  string = raw_input()
  a['size'] = len(string)
  groups = []
  for i in range(len(string) / groupsize):
    groups += [string[i * groupsize:(i + 1) * groupsize]]
  for x in range(groupsize):
    perm = range(1, groupsize + 1)
    perm.remove(x + 1)
    xxx([x + 1], perm)
    
  print "Case #%s: %s" % (case + 1, a['size'])