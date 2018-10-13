import sys
import math

if len(sys.argv)<2:
  exit()
  
def calc(c, f, x):
  a =  int(math.ceil((f*x-2*c)/(c*f)-1))
  if a < 0:
    a = 0
  t = 0

  for i in range(a):
    t += c / (2 + i*f)
  t += x /(2+a*f)
  return t

fname = sys.argv[1]
fn = open(fname, "r")
n = int(fn.readline())

for i in range(0, n):
  c,f,x = [float(y) for y in fn.readline().split()]
  print "Case #%d: %.10f " % (i+1, calc(c, f, x))
  

  

fn.close()

