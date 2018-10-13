def read_int():
  return map(int, raw_input().strip().split())


def solve(r, k, n, gs):
  head = 0
  earning = 0
  for _ in xrange(r):
    i = head
    total = 0
    while total+gs[i] <= k:
      total += gs[i]
      i = (i+1) % n
      if i == head: # one group can only be counted once at one time
        break
    head = i
    earning += total
  return earning


def main():
  nc, = read_int()
  for i in xrange(nc):
    r, k, n = read_int()
    gs = read_int()
    result = solve(r, k, n, gs)
    print 'Case #%d: %s' % (i+1, result)



if __name__ == "__main__":
  main()
