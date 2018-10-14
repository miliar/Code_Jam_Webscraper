#!/Users/apereira/anaconda/bin/python

import sys

def solve(i):
  found = False
  t = int(i)
  while not found or t > 10 :
    u = [int(x) for x in list(str(t))]
    v = sorted(u)
    w = "".join([str(x) for x in v])
    if str(t) == w:
      break
    else:
      t -= 1
  return t

def main(argv=None):
  if argv is None:
    argv = sys.argv
  f = open(sys.argv[1], 'r')
  n = int(f.readline())
  n_case = 1
  while n_case <= n:
    s = solve(int(f.readline()))
    print(f"Case #{n_case}: {s}")
    n_case += 1
  f.close()
  return 0

if __name__ == "__main__":
    sys.exit(main())
