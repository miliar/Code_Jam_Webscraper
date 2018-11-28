from sys import stdin
read = stdin.readline

ints = lambda:map(int,read().split())
doubles = lambda:map(float,read().split())
"""
def find_above(value, start,stop,vals):
  if start == stop:
    return start
  if vals[(start+stop)/2] < value:
    return find_above(value, (start+stop)/2+1, stop,vals)
  return find_above(value,start,(start+stop)/2, vals)

def get_war(girl, boy):
  left = set(boy)
  print left
  for g_i,g in enumerate(girl):
    print "g",g_i,g
    print "b",boy
    b_i = find_above(g, 0,len(boy)-1,boy)
    print b_i
    boy_pick = boy[b_i]
    left -= set([boy_pick])
    print left
    if boy_pick < g:
      break
  else:
    print "AAA:",0
    return 0
  print "BBBB:",len(girl)-g_i
  return len(girl)-g_i
"""

def get_war(girl, boy):
  boy = [b for b in boy]
  left = set(boy)
  #print left
  start = 0
  stop = len(boy)-1
  points = 0
  for g_i,g in enumerate(girl):
    pick = None
    pick_i = None
    for b_i,b in enumerate(boy):

      if b > g and (pick is None or pick - g > b-g):
        pick_i = b_i
        pick = b
    if not pick is None:
      #print "POINT:",pick,">",g
      boy.pop(pick_i)
      
    else:
      #print "NOPNT:",pick,"<",g
      boy.pop(0)
      points += 1
  return points


def get_dwar(girl, boy):
  boy = [b for b in boy]
  girls = set(girl)
  #print left
  start = 0
  stop = len(boy)-1
  points = 0
  for b_i,b in enumerate(reversed(boy)):
    for g_i,g in enumerate(girl):
      pick = None
      pick_i = None
      if g > b and (pick is None or g-b < pick-b):
        pick = g
        pick_i = g_i
    if pick is None:
      girl.pop(0)
    else:
      girl.pop(pick_i)
      points += 1
  return points


def solve():
  N = ints()[0]
  girl = doubles()
  boy  = doubles()
  girlsort = sorted(girl)
  boysort  = sorted(boy)
  #print "SORT:",girlsort
  #print "SORT:", boysort
  war = get_war(girlsort,boysort)
  dwar = 0
  dwar = get_dwar(girlsort,boysort)

  return str(dwar) +" " + str(war)


for t in range(ints()[0]):
  ans = solve()
  print "Case #%d: %s" % (t+1,ans)