import sys

def find_all_paths(graph, start, end, path=[]):
  path = path + [start]
  if start == end:
    return [path]
  if not graph.has_key(start):
    return []
  paths = []
  for node in graph[start]:
    if node not in path:
      newpaths = find_all_paths(graph, node, end, path)
      for newpath in newpaths:
        paths.append(newpath)
  return paths

def main():
  if len(sys.argv)<=1:
      print 'Usage: python A.py <filename>'
      return
  
  arg = sys.argv[1]
  f = open(arg,'r')
  fout = open(arg[:-3]+'out', 'w')
  fr = f.readline()
  fr = fr[:-1]
  for i in range(int(fr)):
    n = int(f.readline())
    graph={}
    flag = 0
    for j in range(n):
      line = f.readline()
      line = line.split()
      m = int(line.pop(0))
      graph[str(j+1)] = line
    for j in range(n):
      for k in range(n):
        if (len(find_all_paths(graph,str(j+1),str(k+1))) >= 2):
          flag = 1
          break
      if(flag):
        break
    if (flag):
      fout.write('Case #'+str(i+1)+': Yes')
    else:
      fout.write('Case #'+str(i+1)+': No')
    if(i<int(fr)-1):
      fout.write('\n')
  return

if __name__ == '__main__':
  main()