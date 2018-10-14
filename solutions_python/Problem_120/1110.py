import math

def solve(**kwargs):
  
  r = kwargs['r']
  t = kwargs['t']
  
  a = float(t)
  
  while (2 * (a ** 2) + (2 * r - 1) * a - t) > 0.0001:
    a -= (2 * (a ** 2) + (2 * r - 1) * a - t) / (4 * a + 2 * r - 1)
  
  return str(int(a))
    

if __name__ == "__main__":
  
  f_in = open('file.in','r')
  f_out = open('file.out','w')

  T = int(f_in.readline())

  for i in range(T):
    
    problem = {}
    
    [problem['r'],problem['t']] = [int(t) for t in f_in.readline().split(' ')]
  
    f_out.write('Case #' + str(i + 1) + ': ' + solve(**problem) + '\n')

  f_in.close()
  f_out.close
  