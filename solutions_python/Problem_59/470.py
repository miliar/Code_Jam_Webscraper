import sys, os
import shutil


T = int(sys.stdin.readline())


def path_dir(x):
  dir_list = x.split('/') 
  dir = dir_list[-1]
  path = '/'.join(dir_list[:-1])
  if not path:
    path = '/'
  return path, dir

def create_dir(full_dir):
  # if it exists do nothing
#  print 'full_dir', full_dir
  if full_dir == '/' or os.path.isdir(full_dir[1:]):
#    print 'terminating'
    return 0
  
  # if it does not exist, make parent then make it
  path, dir = path_dir(full_dir)
#  print 'path:', path, 'dir:', dir
  depth = create_dir(path)
#  print 'making:', full_dir
  os.mkdir(full_dir[1:])
  return depth + 1
  
  

for t in xrange(T):
  os.mkdir('myroot')
  os.chdir('myroot')
  mkdirs = 0
  N, M = map(int, sys.stdin.readline().split())
  
  Nu = []
  for n in range(N):
    thisN = sys.stdin.readline().strip()
    if not os.path.isdir(thisN[1:]):
      os.makedirs(thisN[1:])
        
  for m in range(M):
    thisM = sys.stdin.readline().strip()
    mkdirs += create_dir(thisM)
    
  print "Case #%i: %i" % (t+1, mkdirs)
  

#  os.chdir('..')
#  shutil.rmtree('myroot')