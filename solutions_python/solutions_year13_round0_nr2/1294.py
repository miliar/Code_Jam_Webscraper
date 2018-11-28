
def getMin(field):
  mn = 1000
  for row in field:
    for elem in row:
      if elem < mn:
        mn = elem
  return mn


T = int(input())
for t in range(1, T+1):
  ln = input().split()
  nrows = int(ln[0]) # nrows
  ncols = int(ln[1]) # ncols
  field = []
  for i in range(nrows):
    ln = input().split()
    field.append([int(x) for x in ln])
  
  # while something left
  #  get min
  #  find a row or col with that min
  #   if found: erase it (set to 1000)
  #   if not found: failed
  
  curMin = getMin(field)
  yes = True
  while curMin < 1000:
    # search rows
    found = False
    for r in range(nrows):
      works = True
      something = False
      for c in range(ncols):
        if field[r][c] == curMin:
          something = True
        elif field[r][c] != 1000:
          works = False
          break
      if works and something:
        found = True
        for c in range(ncols):
          field[r][c] = 1000
    # search cols
    if not found:
      for c in range(ncols):
        works = True
        something = False
        for r in range(nrows):
          if field[r][c] == curMin:
            something = True
          elif field[r][c] != 1000:
            works = False
            break
        if works and something:
          found = True
          for r in range(nrows):
            field[r][c] = 1000
    if not found:
      yes = False
      break
    curMin = getMin(field)
  if yes:
    print("Case #" + str(t) + ": YES")
  else:
    print("Case #" + str(t) + ": NO")
  
  
