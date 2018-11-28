import sys
import gmpy # https://pypi.python.org/pypi/gmpy

stdin = sys.stdin

def is_pali(num):
  st = str(num)
  for x in xrange(len(st)/2):
    if st[x] != st[-x-1]:
      return False
  return True
    
  

 
def gen(lst, low_thres, high_thres, pos=0):
  acc = 0
  if pos < (len(lst)+1)/2: # recurse
    for x in xrange(0 if pos else 1,10):
      new_lst = lst[:]
      new_lst[pos] = x
      #print new_lst
      acc += gen(new_lst, low_thres, high_thres, pos+1)
    return acc
  else:
    for z in xrange(len(lst)/2):
      lst[-z-1] = lst[z]
    
    st = ''.join(map(str, lst))
    #print st
    
    num = int(st)
    if num < low_thres or num > high_thres:
      return 0
    
    else:
      return gmpy.is_square(num) and is_pali(gmpy.sqrt(num))
    
    
  
    
  

def doCase(low, high):
  # gen primes between low and high and test for squareness
  
  min_digits = len(str(low))
  max_digits = len(str(high))
  
  total=0
  
  for digits in xrange(min_digits, max_digits+1):
    #print [' ']*digits, digits
    total+=gen([' ']*digits,low,high)
    
  return total
  

num = stdin.readline()

for i in xrange(int(num)):
  low, high = stdin.readline().split(' ')  
  val = doCase(int(low), int(high))
  sys.stdout.write( 'Case #%s: %s\n' % (i+1, val ) )
