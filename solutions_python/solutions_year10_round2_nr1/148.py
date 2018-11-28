import sys

N = int(sys.stdin.readline().strip())


dirs = ['']
dic = {}

for qw in range(1, N+1):
  print 'Case #%d:' % qw,
  ###
  [N1,M1] = sys.stdin.readline().strip().split()
  N1 = int(N1)
  M1 = int(M1)
  for qe in range(1, N1+1):
    dir = sys.stdin.readline().strip()
    dirs.append(dir) 
  cnt = 0  
  for qr in range(1, M1+1):
    dir = sys.stdin.readline().strip()
    dir1 = dir.split('/')
    for d in reversed(range(0,len(dir1))):
      if dirs.count(dir) == 0:
        cnt += 1
        #print dirs,dir,cnt
        dirs.append(dir)
        dir = dir[0:len(dir)-(len(dir1[d])+1)]
  print cnt      
  dirs = ['']  
#  nums = num.split()
#  nums = map(intall, nums)
#  for n in nums:
#  
#  print nums
  ###
  ###
#  result = 0 ##change this
#!!!!
#  print result
#  print 