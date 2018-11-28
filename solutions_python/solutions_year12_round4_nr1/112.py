#!/usr/bin/python
'''
shelajev@gmail.com
'''
import sys
from os.path import abspath
from subprocess import call

DEBUG = 1

def dfs(idx, cur, N, D, d, l, p):
  if(D - d[idx] <= cur):
    return True
  rightmost = None
  for i in range(idx + 1, N):
    if(d[i] - d[idx] > cur):
      rightmost = i - 1
      break
  if rightmost is None:
    rightmost = N - 1
  for i in range(rightmost, idx, -1):
    dx = d[i] - d[idx]
    nl = min(l[i], dx)
    if(p[i] >= nl):
      continue
    p[i] = nl
    if dfs(i, nl, N, D, d, l, p):
      return True
  return False
      
  

def solve(N, D, d, l):
  p = [-1] * N
  p[0] = d[0]
  return dfs(0, d[0], N, D, d, l, p)
#  p = [-1] * N
#  p[0] = d[0]
#  for i in range(1, N):
#    for j in range(i - 1, -1, -1):
#      if(p[i] >= d[i] - d[j]):
#        
#    p[i] = min(l[i], )
#    pass
#  return p[-1] >= D - d[-1]

def main():
  problem = 'A'
  filename = None
  filename = 'input-%s.sample' % problem
  attempt = 1
  filename = '%s-small-attempt%s' % (problem, attempt)
#  filename = '%s-large' % problem
  if not filename:
    input_file = sys.stdin
    output_path = 'sample.txt'
  else:
    input_file = open('in/%s.in' % filename, 'r')
    output_path = 'out/%s.out' % filename
  output_file = open(output_path, 'w')
  T = int(input_file.readline().rstrip())
  for t in range(1, T + 1):
    N = int(input_file.readline().rstrip())
    d, l = [None] * N, [None] * N
    for i in range(N):
      d[i], l[i] = map(int, input_file.readline().rstrip().split())
    D = int(input_file.readline().rstrip())
    
    ans = solve(N, D, d, l)
    msg = 'Case #%s: %s' % (t, "YES" if ans else "NO")
    if filename is None or DEBUG:
      print msg
    output_file.write('%s\n' % msg)
  output_file.close()
  return output_path
    
if __name__ == '__main__':
  output = main()
  print 'Holy Batman! I\'ve just finished crunching it! :)'
  print 'It\'s time to submit!'
  print 'Output file: ', abspath(output)
  call(['cvlc', 'etc/tada.mp3', 'vlc://quit'])
