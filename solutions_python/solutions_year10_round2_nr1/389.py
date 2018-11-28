def read_int():
  return map(int, raw_input().strip().split())


def solve(n, m, existed, new):
  count = 0
  existed_set = {}
  for j in xrange(n):
    path = existed[j].split('/')
    for i in xrange(1, len(path)):
      if i in existed_set:
        existed_set[i].add('/'.join(path[:(i+1)]))
      else:
        existed_set[i] = set()
        existed_set[i].add('/'.join(path[:(i+1)]))
  for j in xrange(m):
    k = 1
    for i in xrange(1, len(new[j])):
        if new[j][i] == '/':
          if k not in existed_set:
            count += 1
            existed_set[k] = set()
            existed_set[k].add(new[j][:i])
          elif new[j][:i] not in existed_set[k]:
            count += 1
            existed_set[k].add(new[j][:i])
          k += 1
  return count


def main():
  nc, = read_int()
  for i in xrange(nc):
     n, m = read_int()
     existed = []
     new = []
     for j in xrange(n):
       existed.append(raw_input().strip())
     for k in xrange(m):
       new.append(raw_input().strip() + '/')
     result = solve(n, m, existed, new)
     print 'Case #%d: %s' % (i+1, result)



if __name__ == "__main__":
  main()
