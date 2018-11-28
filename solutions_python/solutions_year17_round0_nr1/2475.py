import sys

index = -1

for line in sys.stdin.readlines():
  index += 1
  flips = 0

  if index > 0:
    (seq, size) = line.strip().split(' ')
    size = int(size)
    seq = list(seq)
    for c in xrange(len(seq)):
      if seq[c] == '-' and c+size <= len(seq):
        flips = flips + 1
        for cc in xrange(size):
          seq[c+cc] = '-' if seq[c+cc] == '+' else '+'

    print "Case #%i: %s" % (index, flips if not '-' in seq else "IMPOSSIBLE")
