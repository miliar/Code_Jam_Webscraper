
import sys

T = int(sys.stdin.readline())

for t in range(1, T + 1):
  n, k = [int(x) for x in sys.stdin.readline().split()]
  next_pow_two = 1 << k.bit_length()
  offset = k & ~(next_pow_two >> 1)
  max = (n - offset) // next_pow_two
  min = (n - k) // next_pow_two
  print('Case #%d: %d %d' % (t, max, min))
