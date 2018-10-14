f = open("C.in","r")
f2 = open("C.out","w")
T = int(f.readline().strip())

global ex
ex=False
K = {}
solved = []
def check(dd):
  for i in xrange(len(dd)-1):
    for j in xrange(i,len(dd)):
      if ( sum ( [ dd[i][k] * dd[j][k] for k in xrange(20)]  ) == 0 ):
        return [dd[i],dd[j]]
  return False

def selectOrNot(b):
  global ex,solved
  if ( ex ):
    return
  if ( len(b) == 20 ):
    c = sum( [ b[j]*vs[j] for j in xrange(20) ])
    if K.has_key(c):
      K[c].append(b)
      l = check(K[c])
      if l !=False:
        solved = l
        ex = True
    else:
      K[c]= [ b ]
    return 0
  selectOrNot(b+[0])
  selectOrNot(b+[1])


def getSet(vs):
    global K
    K = {}
    global ex,solved
    ex = False
    n = len(vs)
    solved=[]
    out = "Impossible"
          
    selectOrNot( [])
    
    if ( solved != []):
      out = "\n"+' '.join( map(str,filter(lambda x:x>0,[ solved[0][k] * vs[k] for k in xrange(20) ]) )) + "\n" + ' '.join( map(str,filter(lambda x:x>0,[ solved[1][k] * vs[k] for k in xrange(20) ])))
      
    return out


for TT in xrange(T):
    vs = map(int,f.readline().strip().split())[1:]
    
    f2.write( "Case #%d: %s\n" % ((TT+1),getSet(vs) ) )

f2.close()

f.close()

