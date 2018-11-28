#f = open('a.in')
#f = open('../A-small-attempt0.in.txt')
f = open('../A-large.in.txt')
T = int(f.readline())

def inter(l1, l2):
  if (l1 == l2) :
    return None
  '''
  A = y2-y1
B = x1-x2
C = A*x1+B*y1'''
  a1 = l1[1][1] - l1[0][1]
  b1 = l1[0][0] - l1[1][0]
  c1 =  a1*l1[0][0]+b1*l1[0][1]

  a2 = l2[1][1] - l2[0][1]
  b2 = l2[0][0] - l2[1][0]
  c2 =  a2*l2[0][0]+b2*l2[0][1]

  det = a1*b2 - a2*b1
  if det == 0:
    return None
  else :
    x = (b2*c1 - b1*c2) *1.0 /(det*1.0)
    y = (a1*c2 - a2*c1)*1.0 /(det*1.0)
  if x >= min(l1[0][0],l1[1][0]) and x<= max(l1[0][0],l1[1][0]) and x >= min(l2[0][0],l2[1][0]) and x <= max(l2[0][0],l2[1][0]) and y >= min(l1[0][1],l1[1][1]) and y<= max(l1[0][1],l1[1][1]) and y >= min(l2[0][1],l2[1][1]) and y <= max(l2[0][1],l2[1][1]) :
    return (x,y)
  else :
    return None
  
for no in range(T):
  N = int(f.readline())
  lines = []
  for i in range(N):
    l, r = map(int, f.readline().split())
    lines.append(((0,l),(1,r)))
  p = set()
  for l1 in lines:
    for l2 in lines:
      if (None != inter(l1,l2)) :
        p.add(inter(l1,l2))
#  print(p)
  print("Case #{0}: {1}".format(no+1,len(p)))
