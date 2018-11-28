import itertools 
f = open("B.in","r")
f2 = open("B.out","w")
f.readline()

i=1

def check(s,p,sco):
  n = len(sco)
  mmin = p + (p-2)*2
  smax = (p-1)*3
  #exclude mins
  sco = filter(lambda x:x>=mmin and x>=p,sco) 
  candidate = filter(lambda x:x<=smax,sco)

  if ( len(candidate) >= s ):
    return len(sco)-len(candidate)+s
  else:
    return len(sco)


for l in f:
    raw = map(int,l.strip().split())
    n,s,p = tuple(raw[:3])
    scores = raw[3:]

    f2.write( "Case #%d: %s\n" % (i,check(s,p,scores)) )
    i+=1

f2.close()

f.close()
