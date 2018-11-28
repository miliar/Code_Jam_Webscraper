def solve(seq):
  debug = True
  if debug:
    print "Seq", seq
  order = sorted(seq)
  now = order[-1]
  del(order[-1])
  # Find the max element and put p and q there
  for i in xrange(len(seq)):
    if seq[i] == now:
      p = i
      q = i
      break
  # For each element, just move it to the right place in the sequence,
  # by slicing, and count the moves
  count = 0
  while order:
    now = order[-1]
    del(order[-1])
    # Find the location of the current element
    loc = None
    for i in xrange(len(seq)):  
      if seq[i] == now:
        loc = i
        break
    if debug:
      print "Swapping", seq[i]
    # Move it to the nearest location
    if i < p:
      count += p - i - 1
      seq = seq[:i] + seq[i+1:p] + [seq[i]] + seq[p:]
      p -= 1
    else:
      # i > q
      count += i - q - 1
      seq = seq[:q+1] + [seq[i]] + seq[q+1:i] + seq[i+1:]
      q += 1
    if debug:
      print seq
      print count
  return count

def solve2(seq):
  debug = False
  if debug:
    print "Seq", seq
  order = sorted(seq, reverse=True)
  count = 0
  while order:
    now = order[-1]
    del(order[-1])
    # Find the location of the current element
    loc = None
    for i in xrange(len(seq)):  
      if seq[i] == now:
        loc = i
        break
    if debug:
      print "Swapping", seq[i]
    # Move it to the nearest outside location
    if i >= len(seq) / 2:
      count += len(seq) - i - 1
      seq = seq[:i] + seq[i+1:]
    else:
      count += i
      seq = seq[:i] + seq[i+1:]
    if debug:
      print seq
  return count

for tc in xrange(int(raw_input())):
  raw_input() # Lengtj
  items = [int(item) for item in raw_input().split(" ")]
  print "Case #" + str(tc + 1) + ": " + str(solve2(items))

