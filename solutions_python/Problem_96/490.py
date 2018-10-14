#!/usr/bin/python -tt
def main():
  inf = open('input.txt', 'r')
  outf = open('output.txt', 'w')
  n = int(inf.readline())
  for _I in xrange(n):
    outf.write('Case #%d: ' % (_I+1))
    t = [ int(i) for i in inf.readline().split() ]
    N = t[0]
    S = t[1]
    p = t[2]
    t = t[3:]
    res = 0
    for s in t:
      curMin = s/3
      mod = s%3
      if mod:
        curMax = curMin + 1
      else:
        curMax = curMin
      if curMax >= p:
        res += 1
      else:
        if (mod > 1 or (not mod and curMin)) and S:
          S -= 1
          curMax += 1
          if curMax >= p:
            res += 1
          else:
            S += 1
    outf.write('%d\n'%res)

if __name__ == '__main__':
  main()
