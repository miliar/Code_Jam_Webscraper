import sys

def perform_mkdir(root, path):
  to_return = 0
  
  if path[0] not in root["children"]:
    root["children"][path[0]] = {"children":{}}
    to_return += 1
    
  if len(path) > 1:
    subroot = root["children"][path[0]]
    to_return += perform_mkdir(subroot, path[1:])
  
  return to_return
  
filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  params = [int(v) for v in infile.readline().split()]
  N = params[0]
  M = params[1]
  
  root = {"children":{}}

  for n in range(N):
    existing_dir = infile.readline().rstrip().split('/')[1:]
    perform_mkdir(root, existing_dir)
    
  total_needed = 0
  
  for m in range(M):
    new_dir = infile.readline().rstrip().split('/')[1:]
    total_needed += perform_mkdir(root, new_dir)
    
  print total_needed
  
infile.close()