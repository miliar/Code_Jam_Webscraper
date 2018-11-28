##import ???

##fuck the fact that [[n]*k]*k creates multiple reference to the same list
##fuck you very much
def cfill(cboard):
  n = len(cboard)
  adset = set()
  suset = set()
  for row in range(n):
    for col in range(n):
      if cboard[row][col]:
        adset.add(row + col)
        suset.add(row - col)
  fillboard = [[False] * n for i in range(n)]
  for row in [0, n-1]:
    for col in range(n):
      if row + col not in adset and row - col not in suset:
        fillboard[row][col] = True
        adset.add(row + col)
        suset.add(row - col)
  return fillboard
    
def xfill(xboard):
  n = len(xboard)
  rowset = set()
  colset = set()
  for row in range(n):
    for col in range(n):
      if xboard[row][col]:
        rowset |= set([row])
        colset |= set([col])
  fillboard = [[False] * n for i in range(n)]
  for row in range(n):
    for col in range(n):
      if row not in rowset and col not in colset:
        fillboard[row][col] = True
        rowset |= set([row])
        colset |= set([col])
  return fillboard
  
def main():

  ##f1=open(r'C:\Users\mumin\Documents\gcj\testfile.in','r')
  ##f2=open(r'C:\Users\mumin\Documents\gcj\testfile.out','w')  
  f1=open(r'C:\Users\mumin\Documents\gcj\D-small-attempt1.in','r')
  f2=open(r'C:\Users\mumin\Documents\gcj\D-small-attempt1.out','w')
  ##f1=open(r'C:\Users\mumin\Documents\gcj\A-large.in','r')
  ##f2=open(r'C:\Users\mumin\Documents\gcj\A-large.out','w')
  numofcases = int(f1.readline()[:-1])
  linenum = 0
  while linenum < numofcases:
    linenum += 1
    line = f1.readline()
    n = int(line[:line.find(' ')])
    m = int(line[line.find(' ')+1:-1])
    cboard = [[False] * n for i in range(n)]
    xboard = [[False] * n for i in range(n)]
    for i in range(m):
      line = f1.readline()
      mem = line[:-1].split(' ')
      if mem[0] == '+':
        cboard[int(mem[1])-1][int(mem[2])-1] = True
      elif mem[0] == 'x':
        xboard[int(mem[1])-1][int(mem[2])-1] = True
      elif mem[0] == 'o':
        cboard[int(mem[1])-1][int(mem[2])-1] = True
        xboard[int(mem[1])-1][int(mem[2])-1] = True
    cfb = cfill(cboard)
    xfb = xfill(xboard)
    changes = []
    score = 0
    for row in range(n):
      for col in range(n):
        score += xboard[row][col] + cboard[row][col] + xfb[row][col] + cfb[row][col]
        if cfb[row][col]:
          if xboard[row][col] or xfb[row][col]:
            changes.append('o {} {}'.format(row+1, col+1))
          else:
            changes.append('+ {} {}'.format(row+1, col+1))
        elif xfb[row][col]:
          if cboard[row][col]:
            changes.append('o {} {}'.format(row+1, col+1))
          else:
            changes.append('x {} {}'.format(row+1, col+1))
    f2.write('Case #{}: {} {}\n'.format(linenum, score, len(changes)))
    for change in changes:
      f2.write(change + '\n')

  f1.close()
  f2.close()   

if __name__ == '__main__':
  main()