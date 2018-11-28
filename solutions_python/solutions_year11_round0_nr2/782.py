import sys
from collections import defaultdict

def main(args):
  C = int(raw_input())
  for c in range(1, C+1):
    line = raw_input().split()
    D = int(line[0])
    combine = defaultdict(str)
    for i in range(1, D+1):
      combine[line[i][:2]] = line[i][2]
      combine[line[i][:2][::-1]] = line[i][2]
    N = int(line[D+1])
    opposed = defaultdict(str)
    for i in range(D+2, D+N+2):
      opposed[line[i]] = True
      opposed[line[i][::-1]] = True
    S = line[-1]
    O = ""
    for s in S:
      O += s
      if len(O) > 1 and combine[O[-2:]]:
        O = O[:-2] + combine[O[-2:]]
      else:
        for i in range(len(O)-1):
          if opposed[O[i] + s]:
            O = ""
            break
    print "Case #%d: [%s]" % (c, ', '.join(O))

if __name__ == '__main__':
  main(sys.argv)
