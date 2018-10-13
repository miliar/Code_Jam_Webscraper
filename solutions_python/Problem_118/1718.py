import math

def solve(**kwargs):
  
  interval = kwargs['interval']
  count = 0
  
  for i in range(interval[0],interval[1] + 1):
    if isPalyndrome(i) and isSquare(i) and isPalyndrome(int(math.sqrt(i))):
      count += 1
  
  return str(count)

def isSquare(x):
  return int(math.sqrt(x)) == math.sqrt(x)

def isPalyndrome(x):
  x = str(x)
  ox = [c for c in str(x)]
  rx = [c for c in str(x)]
  rx.reverse()
  return ox == rx

if __name__ == "__main__":
  
  f_in = open('file.in','r')
  f_out = open('file.out','w')

  T = int(f_in.readline())

  for i in range(T):
    
    problem = {}
    
    problem['interval'] = [int(t) for t in f_in.readline().split(' ')]
    
    f_out.write('Case #' + str(i + 1) + ': ' + solve(**problem) + '\n')

  f_in.close()
  f_out.close