from fractions import gcd

IN = open("in", 'r')
OUT = open("out", 'w')

n = IN.readline()

def lcm(numbers):
    return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)

def index_min(values):
    return min(xrange(len(values)),key=values.__getitem__)


for x in xrange(1, int(n)+1):
  line = map(int, IN.readline().strip().split(' ')) 
  M = map(int, IN.readline().strip().split(' ')) 
  B = line[0]
  N = line[1]
  
  Ma = [0] * len(M)
  Na = 1
  idx = 0
  
  leCoMu = lcm(M)
  
  PPL = 0
  for i in range(0, B):
    PPL += leCoMu / M[i]
  
  res = N % PPL
  
  if res != 0:
    N = res
  else:
    N = PPL
    
  while N >= Na:
    idx = index_min(Ma)
    Ma[idx] +=  M[idx]
    Na += 1
  
    
  outline = "Case #" + str(x) + ": " + str(idx+1) + "\n"
  print outline
  OUT.write(outline)


OUT.close()
IN.close()