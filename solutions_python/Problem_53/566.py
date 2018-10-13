#!/local/usr/bin/python2.5

import sys

def tobin(n):
  h2b = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
  	     '4': '0100', '5': '0101', '6': '0110', '7': '0111',
	     '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
	     'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
  h = '%x' % n
  b = ''
  for digit in h:
    b += h2b[digit]
  return b

T = int(sys.stdin.readline().strip())

for i in range(T):
  n, k = tuple([int(x) for x in sys.stdin.readline().split()])
  result = tobin(k % (2**n))[-n:]
  if result[0] == '1':
    print 'Case #%d: ON' % (i+1)
    continue
  print 'Case #%d: OFF' % (i+1)
