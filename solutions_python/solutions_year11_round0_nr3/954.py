



def Contest(file):
  f=open(file,'r')
  count = int(f.readline()[:-1])
  for i in range(1,count+1):
    f.readline() # just forget that line
    s = map(lambda x:int(x),f.readline()[:-1].split(' '))
    print "Case #%d:" % (i),candy(s)
  f.close()

def candy(s):
  s.sort()
  if reduce(lambda x,y:x^y, s) == 0:
    return reduce(lambda,x,y:x+y,s[1:])
  return "NO"





