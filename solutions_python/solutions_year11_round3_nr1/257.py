N = input()
for k in range(N):
  R, C = map(int, raw_input().split())
  picture = []
  for r in range(R):
    picture.append(list(raw_input()))
  
  for r in range(R-1):
    for c in range(C-1):
      if picture[r][c] == picture[r+1][c+1] == picture[r][c+1] == picture[r+1][c] == '#':
        picture[r][c] = '/'
        picture[r][c+1] = '\\'
        picture[r+1][c] = '\\'
        picture[r+1][c+1] = '/'

  possible = True
  for r in range(R):
    for c in range(C):
      if picture[r][c] == '#':
        possible = False
        break
  
  print "Case #%d:" % (k+1)
  if not possible:
    print "Impossible"
  else:
    for row in picture:
      print ''.join(row)

