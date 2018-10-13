def power_of_two(x):
  return x and not x-1 & x

def all_ones(x, n):
  # If it's not zero and the last n bits are all one
  return x and power_of_two((x & 2**n-1)+1) and 2**n-1 == (x & 2**n-1)

if __name__ == "__main__":
  cases = int(raw_input())
  for cnum in xrange(1, cases+1):
    n, k = map(int, raw_input().split())
    print "Case #%d: %s" % (cnum, "ON" if all_ones(k, n) else "OFF")
