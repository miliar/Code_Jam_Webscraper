import argparse
from math import ceil

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', help="input_file")
parser.add_argument('-o', '--output', help="output_file")
args = parser.parse_args()


def solve(data1, data2):
  t = int(data1[0])
  n = [int(i) for i in data2]
  assert len(n) == t
  diff = []
  for i in xrange(len(n) - 1):
    diff.append(max(n[i] - n[i + 1], 0))
  ans1 = sum(diff)
  ans2 = 0
  m = max(diff)
  for i in xrange(len(n) - 1):
    ans2 += min(n[i], m)
  return '%s %s' % (ans1, ans2)

with open(args.input, 'r') as inf, open(args.output, 'w') as outf:
  n = int(inf.next())
  c = 0
  for line in inf:
    c += 1
    ans = solve(line.strip().split(), inf.next().strip().split())
    print >> outf, "Case #%s: %s" % (c, ans)
    n -= 1

assert n == 0
