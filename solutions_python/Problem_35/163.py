import sys
import logging
logging.basicConfig(level=logging.WARNING, format="%(levelname)-8s: %(message)s - %(pathname)s:%(lineno)d")

def parse_params(f):
  return map(int,f.readline().split())

input = len(sys.argv)>1 and open(sys.argv[1]) or sys.stdin

def neighbours(map,x,y):
  H=len(map)
  W=len(map[0])
  alt = map[y][x]
  if y>0 and map[y-1][x]<alt: yield x, y-1
  if x>0 and map[y][x-1]<alt: yield x-1, y
  if x<W-1 and map[y][x+1]<alt: yield x+1, y
  if y<H-1 and map[y+1][x]<alt: yield x, y+1

def drop(map, labels, x, y):
  if labels[y][x]!=None: 
    return labels[y][x]
  
  neigh = [k for k in neighbours(map,x,y)]
  if neigh:
    nx, ny = min(neigh,key=lambda k:map[k[1]][k[0]])
    if map[ny][nx] < map[y][x]:
      labels[y][x] = drop(map, labels, nx, ny)
      return labels[y][x]

  global label
  labels[y][x] = label
  label = chr(ord(label)+1)
  return labels[y][x]
  
T, = parse_params(input)

for t in xrange(T):
  H, W = parse_params(input)
  logging.info('map %d, %dx%d',t+1,W,H)
  height_map = []
  labels = []
  label = 'a'

  for h in xrange(H):
    height_map.append(parse_params(input))
    labels.append([None]*W)

  for y in xrange(H):
    for x in xrange(W):
      drop(height_map, labels, x, y)
      
  print "Case #%d:"%(t+1)
  for row in labels:
    print ' '.join(row)

