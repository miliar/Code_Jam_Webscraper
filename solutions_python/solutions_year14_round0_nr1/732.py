import sys

inp = sys.stdin

def getResult(intersection):
  if(len(intersection)==1): return str(intersection.pop())
  if(len(intersection)>1): return "Bad magician!"
  if(len(intersection)==0): return "Volunteer cheated!"
  

T=int(inp.readline())
for t in range(1,T+1):
    i=int(inp.readline())
    for x in range(1,5):    
      ls= [int(y) for y in inp.readline().split()]
      if x==i: a=set(ls)
    i=int(inp.readline())
    for x in range(1,5):
      ls= [int(y) for y in inp.readline().split()]
      if x==i: b=set(ls)
    print "Case #%d: %s" % (t,getResult(a&b))

