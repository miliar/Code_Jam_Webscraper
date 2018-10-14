import sys
import numpy
from cStringIO import StringIO


stdin = sys.stdin

def test_array(arr, pt_idx):
    pt = arr[pt_idx]
    #print pt_idx, pt, arr
    
    try:
      max_l = max(arr[:pt_idx])
    except ValueError:
      max_l = -1
      
    try:
      max_r = max(arr[pt_idx+1:])
    except ValueError:
      max_r = -1
    #print max_l, max_r
    
    return pt >= max_l and pt>= max_r
    
  

def doCase(N, M):
  new_str = ''
  for x in xrange(N):
    new_str+=stdin.readline() + '\n'
    
  a = numpy.loadtxt(StringIO(new_str), dtype=numpy.int)
  #print a
  
 
  # test all points:
  if N==1 or M==1: # special case
    return True
  
  for x in xrange(N):
    for y in xrange(M):
      #print x, y
      #print a[x,y], a[x], a[:,y]
      still_possible = test_array(a[x],y) or test_array(a[:,y],x)
      if not still_possible:
	return False
      
    
  
  
  return True
    
  
  

num = stdin.readline()

#print num

for i in xrange(int(num)):
  N, M = stdin.readline().split(' ')  
  val = doCase(int(N), int(M))
  sys.stdout.write( 'Case #%s: %s\n' % (i+1, 'YES' if val else 'NO' ) )