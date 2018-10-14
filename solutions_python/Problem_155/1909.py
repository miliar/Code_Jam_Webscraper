import sys

if __name__ == '__main__':
  count0 = int(sys.stdin.readline())
  for ci in range(count0):
    [smax, slist] = sys.stdin.readline().split()
    smax = int(smax)
    audnum = 0
    res = 0
    for shyness in range(smax + 1):
      aud = ord(slist[shyness]) - ord('0')
      if aud != 0:
        if audnum < shyness:
          res += shyness - audnum
          audnum = shyness
        audnum += aud
    cn = ci+1
    print('Case #%d: %d' % (cn, res))