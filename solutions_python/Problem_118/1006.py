import numpy as np
from math import ceil, sqrt

fin = open('C-small-attempt0.in')
fout = open('out_small.txt', 'w')

def isqrt(x):
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

T = int(fin.readline().rstrip('\n'))

def IsPalindrome(x):
  return(str(x)[::-1] == str(x))

for iter in range(T):
  num_palindromes = 0
  num_lims = np.array(fin.readline().rstrip('\n').split(), dtype=long)
  min_val = num_lims[0]
  max_val = num_lims[1]
  start_val = int(ceil(sqrt(min_val)))
  for i in range(start_val, isqrt(max_val)+1,1):
    if IsPalindrome(i) and IsPalindrome(pow(i,2)):
      num_palindromes = num_palindromes + 1
  case_num = iter+1
  fout.write('Case #%d: ' %case_num + '%d\n' %num_palindromes)
    
fin.close()
fout.close()