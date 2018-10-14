# Hmmm... python...
def arrows(m,rs,cs):
  for row in range(rs):
    for col in range(cs):
     cell = m[row][col]
     min = cell[0]
     cell[1] = None
     for (r,c) in neighboursOf(row,col,rs,cs):
        if m[r][c][0] < min:
            min = m[r][c][0]
            cell[1] = (r,c)
  return m

def neighboursOf(row,col,r,c):
  if row > 0: yield (row-1,col)
  if col > 0: yield (row,col-1)
  if col < c-1: yield (row,col+1)
  if row < r-1: yield (row+1,col)


def findBasins(m,rs,cs):
    char = 97
    for row in range(rs):
        for col in range(cs):
            c = col
            r = row
            cell=m[r][c]
            list = [cell]
            while cell[1] and not cell[2]:
                (r,c) = cell[1]#;print (r,c),
                cell=m[r][c]
                list+=[cell]
            if cell[2]:
                for cell2 in list: cell2[2] = cell[2]
            else:
                for cell in list:
                    cell[2] = chr(char)
                char+=1
    return m

def fill(m,rs,cs):
  for row in range(rs):
    for col in range(cs):
        n = m[row][col]
        m[row][col] = [n,None,None]
  return m


input = open("b.large.in")
n = int(input.readline())
for case in range(n):
	(r,c) = map(int,input.readline().split())
	m = []
	for row in range(r):
		m += [map(int,input.readline().split())]


	m = fill(m,r,c)
	m = arrows(m,r,c)
	m = findBasins(m,r,c)
	print "Case #%i:" % (case+1)
	for r in m:
  		for i in r: print i[2],
  		print
