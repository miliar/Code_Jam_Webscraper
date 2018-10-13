fin = open('A-small.in', 'r')
fout = open('A-small.out', 'w')

T = int(fin.readline())

def mintree(tree, i, M, v):
  if i < (M-1)/2:
    lt = mintree(tree, i*2+1, M, True)
    lf = mintree(tree, i*2+1, M, False)
    rt = mintree(tree, i*2+2, M, True)
    rf = mintree(tree, i*2+2, M, False)

    if tree[i][0] == 0:
      if tree[i][1] == 0:
        if v:
          return min(lt+rf,lf+rt,lt+rt)
        else:
          return lf+rf
      else:
        if v:
          return min(lt+rf,lf+rt,lt+rt)
        else:
          return min(lf+rf,lt+rf+1,lf+rt+1)
    else:
      if tree[i][1] == 0:
        if v:
          return lt+rt
        else:
          return min(lt+rf,lf+rt,lf+rf)
      else:
        if v:
          return min(lt+rt,lt+rf+1,lf+rt+1)
        else:
          return min(lt+rf,lf+rt,lf+rf)
  else:
    if tree[i] == v:
      return 0
    else:
      return 40

def calc(tree, i, M):
  if i < (M-1)/2:
    if tree[i][0] == 1:
      return calc(tree,i*2+1,M) and calc(tree,i*2+2,M)
    else:
      return calc(tree,i*2+1,M) or calc(tree,i*2+2,M)
  else:
    return tree[i]  

for i in range(T):
  (M, V) = map(int, fin.readline().split(' '))
  tree = [0] * M

  j = 0
  for k in range((M-1)/2):
    (G, C) = map(int, fin.readline().split(' '))
    print i+1
    print j
    print M
    tree[j] = (G, C)
    j = j + 1

  j = (M-1)/2
  for k in range((M+1)/2):
    Z = int(fin.readline())
    tree[j] = bool(Z)
    j = j + 1

  bf = mintree(tree, 0, M, bool(V))

  if bf > 30:
    fout.write('Case #' + str(i + 1) + ': ' + 'IMPOSSIBLE' + '\n')
  else:
    fout.write('Case #' + str(i + 1) + ': ' + str(bf) + '\n')
