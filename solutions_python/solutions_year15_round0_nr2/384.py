import argparse
from math import ceil

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', help="input_file")
parser.add_argument('-o', '--output', help="output_file")
args = parser.parse_args()

def ncut(n, cnts):
  # Compute number of cuts for height of n
  cuts = 0
  for h in range(n + 1, len(cnts)):
    cuts += int(round(ceil((h - n) / (1.0 * n)))) * cnts[h]
  return cuts


def solve(data1, data2):
  diners = int(data1[0])
  plates = [int(i) for i in data2]
  assert len(plates) == diners 
  cnts = [0] * (max(plates) + 1)
  for p in plates:
    cnts[p] += 1
  min_time = max(plates)
  for h in range(1, max(plates)):
    time = h + ncut(h, cnts)
    min_time = min(min_time, time)
  return min_time

with open(args.input, 'r') as inf, open(args.output, 'w') as outf:
  n = int(inf.next())
  c = 0
  for line in inf:
    c += 1
    ans = solve(line.strip().split(), inf.next().strip().split())
    print >> outf, "Case #%s: %s" % (c, ans)
    n -= 1

assert n == 0
