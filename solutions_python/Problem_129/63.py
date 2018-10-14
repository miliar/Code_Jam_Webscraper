import math

fin = open('in1.txt','r')
fout = open('out1.txt','w')

T = int(fin.readline().strip())

#Functions in here
def costs(o,e):
  k = e-o
  return k*N-k*(k-1)/2

def easy_total(pairs,N):
  cost = 0
  for o,e,p in pairs:
    cost = cost + p*costs(o,e)
  return cost

def get_origin(p):
  return p[0]

#no time to do this efficiently =P
def worst_total(pairs,N):
  tickets = []
  cost = 0
  for k in range(1,N+1):
    for o,e,p in pairs:
      #add in tickets for everyone getting on
      if o==k:
        for i in range(p):
          tickets.append((o,e))
    for o,e,p in pairs:
      #remove tickets for everyone getting off, and pay them
      if e==k:
        for i in range(p):
          t = tickets.pop()
          cost = cost + costs(t[0],k)
  return cost

for idx in range(T):
  N,M = [long(a) for a in fin.readline().strip().split(' ')]
  #pairs is o e p
  pairs_f = [fin.readline().strip() for i in range(M)]
  pairs = []
  for p in pairs_f:
    pairs.append([int(a) for a in p.split(' ')])

    
  ans = easy_total(pairs,N)-worst_total(pairs,N)
  out = "Case #" + str(idx+1) + ": " + str(ans) + "\n"
  fout.write(out)

fin.close()
fout.close()
