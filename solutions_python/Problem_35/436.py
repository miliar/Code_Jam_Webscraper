def load(name):
  f = file(name)
  s = f.readlines()
  f.close()
  return s
  
def neighbors(i, j, w, h):
  r = [(i + x, j + y) for x, y in [(0, -1), (-1, 0), (1, 0), (0, 1)]]
  return [t for t in r if t[0] < w and t[1] < h and t[0] >= 0 and t[1] >= 0]
  
def set(s, basins):
  r = [s]
  for t in basins[s]:
    r.extend(set(t, basins))
  return r
  
def case(area, w, h):
  sinks = []
  basins = dict([((i, j), []) for j in range(h) for i in range(w)])
  area = dict([((i, j), area[j][i]) for j in range(h) for i in range(w)])
  for j in range(h):
    for i in range(w):
      k = (i, j)
      n = neighbors(i, j, w, h)
      if len(n) > 0:
        low = min(n, key=lambda t: area[t])
        if area[low] < area[k]:
          basins[low].append(k)
        else:
          sinks.append(k)
      else:
        sinks.append(k)
  drains = [set(s, basins) for s in sinks]
  
  ltr = 'a'
  r = [['' for i in range(w)] for j in range(h)]
  coord = [(i, j) for j in range(h) for i in range(w)]
  while len(drains) > 0:
    for d in drains:
      if coord[0] in d:
        drains.remove(d)
        for t in d:
          r[t[1]][t[0]] = ltr
          coord.remove(t)
        ltr = chr(ord(ltr) + 1)
        break
  return r
  
def main():
  lines = load('B-small.in')
  n = int(lines[0])
  i = 1
  for c in range(n):
    h, w = [int(t) for t in lines[i].split()]
    data = case([l.split() for l in lines[i + 1: i + h + 1]], w, h)
    i += h + 1
    print 'Case #%d:' % (c + 1)
    print '\n'.join([' '.join(r) for r in data])

if __name__ == '__main__':
  main()
