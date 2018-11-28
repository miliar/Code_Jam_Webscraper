import numpy as np
from sys import argv

#in_file_name = 'snapper-test.in'
out_file_name = 'snapper-large.out'


def solve():
  with open(in_file_name) as in_file:
    in_data = in_file.read().split('\n')
  
  T = int(in_data.pop(0))
  out_data = []

  for t in xrange(T):
    N, K = [int(this) for this in in_data.pop(0).split()]
    
    if K >= N:
      light_on = not bool((K+1) % 2**N)
    else:
      light_on = False
      
    out_data.append("Case #%i: %s \n" % (t+1, "ON" if light_on else "OFF") )
    
    
  assert T == len(out_data) 
  
  with open(out_file_name, 'w') as out_file:
    out_file.writelines(out_data)
    
  
def test():
  N, K = 6, 9
  return get_light_state(N, K)


if __name__ == '__main__':
  in_file_name = argv[1] 
  solve()
  
#  print test()
  print 'done'