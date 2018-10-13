
def foo(trees):
  v1 = trees #[x for x in trees]
  v2 = []
  count = 0
  
  for i in range(len(trees)):
    v2.append([])
    #add a new vertex to current trees
    for j in range(len(trees)):
      if i != j:
        v2[i].append(trees[j])
  
  #print 'V1:', v1
  #print 'V2:',v2
  
  for i in range(len(v1)):
    for j in range(len(v2[i])):
      for k in range(len(trees)):
        if trees[k] != v2[i][j] and trees[k] != v1[i]:
          if (v1[i][0] + v2[i][j][0] + trees[k][0]) % 3 == 0:
            if (v1[i][1] + v2[i][j][1] + trees[k][1]) % 3 == 0:
              count += 1
  
  return count/6


N = int(raw_input())

for i in range(1, N+1):
  n, A, B, C, D, x0, y0, M = map(int, raw_input().split())
  
  X = x0
  Y = y0
  bar = [[X,Y]]
  for ii in range(n-1):
    X = (A * X + B) % M
    Y = (C * Y + D) % M
    bar.append([X, Y])
  
  print 'Case #%d: %d' % (i, foo(bar))
