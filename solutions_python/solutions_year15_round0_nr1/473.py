import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-i', '--input', help="input_file")
parser.add_argument('-o', '--output', help="output_file")
args = parser.parse_args()

def solve(data):
  n = int(data[0])
  arr = [int(i) for i in data[1]]
  assert len(arr) == n + 1
  invited = 0
  sum = 0
  for i in range(len(arr)):
    if sum + invited < i:
      invited += i - sum - invited
    sum += arr[i]
  return invited

with open(args.input, 'r') as inf, open(args.output, 'w') as outf:
  n = int(inf.next())
  c = 0
  for line in inf:
    c += 1
    ans = solve(line.strip().split())
    print >> outf, "Case #%s: %s" % (c, ans)
    n -= 1

assert n == 0
