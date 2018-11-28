fname = "A-large.in"
# fname = "test.in"

def solve(MAX, ppl):
  csum = 0
  margin = 0
  for j in xrange(int(MAX)+1):
    csum += int(ppl[j])
    margin = max(margin, j + 1 - csum)
  return margin

def main():
  with open(fname) as f:
    for i in xrange(int(f.readline())):
      MAX, ppl = f.readline().split()
      print 'Case #%s: %s' % (i + 1, solve(MAX, ppl))

main()