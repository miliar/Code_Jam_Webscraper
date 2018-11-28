# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for c in range(1, t + 1):
  n,r,o,y,g,b,v = map(int, input().split(" "))  # read a list of integers, 2 in this case
  
  l = {'R':r, 'O':o, 'Y': y, 'G': g, 'B': b, 'V': v}
  neigh = {'R': 'BGY', 'O': 'VGB', 'Y': 'BVR', 'G': 'VRO', 'B': 'ROY', 'V': 'OYG'}


  # pierwszy nie ma znaczenia
  can = True
  res = ""
  m = max(l, key=l.get)
  res += m
  l[m] = l[m] - 1


  # potem najdluzszych cykli
  visited = {'R': -1, 'O':-1, 'Y': -1, 'G': -1, 'B': -1, 'V': -1}
  visited[m] = 0

  for i in range(n-1):
    prev = res[-1]
    nex = dict((k, l[k]) for k in neigh[prev] if l[k])
    if not nex:
      can = False
      break
    m = min(nex, key=visited.get)
    res += m
    visited[m] = i
    l[m] = l[m] - 1

  if can and n > 1:
    can = res[-1] in neigh[res[0]]

  print("Case #{}: {}".format(c, res if can else "IMPOSSIBLE"))
