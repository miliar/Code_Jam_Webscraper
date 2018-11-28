def read_int():
  return map(int, raw_input().strip().split())


def solve(n, lines):
  count = 0
  for i in xrange(n):
    for j in xrange(i+1, n):
      if lines[i][0] > lines[j][0] and lines[i][1] < lines[j][1] or lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1]: 
        count += 1;
  return count


def main():
  nc, = read_int()
  for i in xrange(nc):
    n, = read_int()
    lines = []
    for j in xrange(n):
      lines.append(read_int())
    result = solve(n, lines)
    print 'Case #%d: %s' % (i+1, result)



if __name__ == "__main__":
  main()
