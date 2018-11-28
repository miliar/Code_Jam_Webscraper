"""
Input
4
4 11111
1 09
5 110011
0 1

Output
Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
"""

import sys

def read(filen, fileout):
  T = 0
  cases = []
  trial = 0
  with open(filen) as f:
    with open(fileout, 'w') as fout:
      T = int(f.readline())
      for line in f:
        if len(line.split()) > 1:
          trial += 1
          s_max = int(line.split()[0])
          s = [ int(i) for i in list(line.split()[1]) ]
          ans = solve_it(s_max, s)
          fout.write('Case #{0}: {1}\n'.format(trial,ans))

def solve_it(s_max, s):
  curr_s = 0        # The initial amount of 'ovation'
  needed = 0        # How many more ovations we need
  for i in range(len(s)):
    if i > curr_s:  # There's not enough ovation for the remainder to stand
      needed += i-curr_s
      curr_s += i-curr_s    # In the case that there were enough...
    curr_s += s[i]
  return needed
        
def main(filen, fileout):
  read(filen, fileout)
  


if __name__ == '__main__':
  if len(sys.argv) == 3:
    main(sys.argv[1], sys.argv[2])
  else:
    print('Wrong number of arguments')
