# Lawnmower

i = open("B-small-attempt1.in", "r")
o = open("B-small.out", "w")

T = int(i.readline())

def trimX(a, x, h, M):
  for y in range(M):
    a[x][y] = h
  return a

def trimY(a, y, h, N):
  for x in range(N):
    a[x][y] = h
  return a

for c in range(1, T + 1):
    N, M = map(int, i.readline().replace('\n','').split())

    a = []
    for x in range(N):
      a.append(map(int, i.readline().replace('\n','').split()))

    lawn = [[2 for y in range(M)] for x in range(N)]
    diff = [[2 - a[x][y] for y in range(M)] for x in range(N)]

    spots = []
    for x in range(N):
      for y in range(M):
        if diff[x][y] == 1:
          spots.append((x,y))

    for x in range(N):
      if diff[x] == [1]*M:
        for y in range(M):
          if (x, y) in spots:
            spots.remove((x,y))

    for y in range(M):
      if [item[y] for item in diff] == [1]*N:
        for x in range(N):
          if (x, y) in spots:
            spots.remove((x,y))

    result = "YES" if spots == [] else "NO"

    o.write("Case #{0}: {1}\n".format(c, result))

i.close()
o.close()