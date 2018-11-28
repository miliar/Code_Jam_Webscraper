from collections import defaultdict

def iterate(seq, base):
  combines = False
  if seq:
    for c in combine_dict[seq[-1]]:
      if c[0] == base:
        combines = True
        break
  if combines:
    seq = seq[:-1]
    seq = iterate(seq, c[1])
  else:
    opposed = False
    for o in oppose_dict[base]:
      if o in seq:
        opposed = True
        break
    if opposed:
      seq = ''
    else:
      seq += base
  return seq

for case in xrange(1, int(raw_input())+1):
  line = raw_input().split()
  C = int(line[0])
  combine = line[1:1+C]
  combine_dict = defaultdict(list)
  for c in combine:
    combine_dict[c[0]] += [(c[1], c[2])]
    combine_dict[c[1]] += [(c[0], c[2])]
  line = line[1+C:]
  D = int(line[0])
  oppose = line[1:1+D]
  oppose_dict = defaultdict(list)
  for o in oppose:
    oppose_dict[o[0]] = o[1]
    oppose_dict[o[1]] = o[0]
  line = line[1+D:]
  N = int(line[0])
  bases = line[1]

  seq = ''
  for base in bases:
    seq = iterate(seq, base)

  print "Case #%d: [%s]" % (case, ', '.join(seq))
