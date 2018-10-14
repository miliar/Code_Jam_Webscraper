import re
fin = "A-large.in"
fout = open(fin.replace("in","out"),"w")
fin  = open(fin)

T = int(fin.readline())
for t in range(1,T+1):
  RC = fin.readline().split(" ")
  R,C = int(RC[0]),int(RC[1])
  cells = []
  print >>fout, ("Case #%d:" % t)
  for r in range(R):
    cells.append(list(fin.readline().strip()))
  impossible = False
  print cells
  for r in range(R):
    if impossible:
      break
    for c in range(C):
      if impossible:
        break
      if cells[r][c]=="#":
        if c+1 < C and r+1 < R:
          if cells[r][c+1]=="#" and cells[r+1][c]=="#" and cells[r+1][c]=="#":
            cells[r][c] = "/"
            cells[r][c+1] = "\\"
            cells[r+1][c] = "\\"
            cells[r+1][c+1] = "/"
          else:
            impossible = True
        else:
          impossible = True
  if impossible:
    print >>fout, "Impossible"
  else:
    out = "\n".join(["".join(row) for row in cells])
    if re.match(r"#",out):
      print >>fout, "Impossible"
    else:
      print >>fout, out
    