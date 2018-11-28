import sys

def main():
  cases = int(sys.stdin.readline())
  for case in xrange(cases):

    line = sys.stdin.readline().strip().split(' ')
    n = int(line[0])
    k = line[1].strip()

    t = 0
    f = 0
    for i in xrange(n + 1):
      req = int(k[i])
      if req > 0 and t < i:
        f += i - t
        t += f
      t += req

    print("Case #%d: %d" % (case + 1, f))

main()
