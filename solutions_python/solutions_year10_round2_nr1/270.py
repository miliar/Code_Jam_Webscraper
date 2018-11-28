def createPath(diction, path):
    count = 0
    assert isinstance(path, list)
    current= diction
    for i in path:
      if i not in current:
        current[i] = {}
        count+=1
      current = current[i]
    return count
      


for i in range(1, int(raw_input())+1):
  directory = {}
  N, M = map(int, raw_input().split())
  for j in range(N):
    dir = raw_input().split('/')[1:]
    createPath(directory, dir)
  count = 0
  for j in range(M):
    dir = raw_input().split('/')[1:]
    count += createPath(directory, dir)
  print 'Case #%d: %d' % (i, count)
