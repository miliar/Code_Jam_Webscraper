import heapq

def split(n, k):
  level = [(n, 1)]
  total = 0
  while True:
    if len(level) == 1:
      slot, count = level[0]
      total += count
      if total >= k:
        return slot / 2, (slot - 1) / 2
      if slot % 2 == 0:
        level = [(slot / 2, count), (slot / 2 - 1, count)]
      else:
        level = [(slot / 2, 2 * count)]
    else:
      total += level[0][1]
      if total >= k:
        slot = level[0][0]
        return slot / 2, (slot - 1) / 2
      total += level[1][1]
      if total >= k:
        slot = level[1][0]
        return slot / 2, (slot - 1) / 2

      a = level[0][0] / 2
      b = a - 1
      if level[0][0] % 2 == 1:
        level = [(a, 2 * level[0][1] + level[1][1]), 
                 (b, level[1][1])]
      else:
        level = [(a, level[0][1]),
                 (b, 2 * level[1][1] + level[0][1])]

def solve(name):
  f = open(name, 'r')
  c = int(f.readline())
  for i in xrange(c):
    n, k = f.readline().split(' ')
    l, r = split(int(n), int(k))
    print 'Case #%d: %d %d' % (i + 1, l, r)
  f.close()

def main():
  solve('C-large.in.txt')

if __name__ == '__main__':
  main()
    
