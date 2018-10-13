cases = int(raw_input())
for i in xrange(1, cases+1):
  print "Case #%d:" %i,
  input = raw_input()
  conv = {}
  next_val = 1
  for c in input:
    if not conv.has_key(c):
      conv[c] = next_val
      if next_val >= 2:
        next_val += 1
      elif next_val == 1:
        next_val = 0
      elif next_val == 0:
        next_val = 2
      else:
        print "this can't happen!"

  base = len(conv.keys())
  if base == 1:
    base = 2
  #print base
  #print conv
  result = 0
  for c in input:
    result = result * base + conv[c]
  print result
