test_cases = int(raw_input())

def solve(t):
  #def get_max(lawn):
  #  return max( max(e for e in row) for row in lawn)
  def fill(y,x,lawn,elawn,value,dx,dy):
    o_y = y
    o_x = x
    can_cut = True
    while y >=0 and y < len(lawn) and x >= 0 and x < len(lawn[0]) :
      if elawn[y][x] > value:
	can_cut = False
	return;
      y += dy
      x += dx
    x = o_x
    y = o_y
    while y >=0 and y < len(lawn) and x >= 0 and x < len(lawn[0]) :
      lawn[y][x] = value
      y += dy
      x += dx
  n,m = map(int,raw_input().split())
  elawn = [map(int,raw_input().split()) for i in xrange(n) ]
  lawn = [[100 for i in xrange(m)] for i in xrange(n)]
  values = set()
  for row in elawn:
    values |= set(row)
  for v in sorted(values,reverse=True):
    #for each edge point, try to fill in as much as possible 
    for i in xrange(m):
      fill(0, i, lawn,elawn, v,0,1)
      fill(n-1,i,lawn,elawn, v,0,-1)
    for i in xrange(n):
      fill(i,0, lawn,elawn, v,1,0)
      fill(i,m-1,lawn,elawn,v,-1,0)
  if lawn != elawn:
    print "Case #{}:".format(t) + " NO"
  else:
    print "Case #{}:".format(t) + " YES"

    
for n in xrange(test_cases):
  solve(n+1)