import string
def readFile():
  triggerfile = open("A-large.in", "r")
  all = [ line.rstrip() for line in triggerfile.readlines() ]
  lines=[]
  for line in all:
    a=[]
    for letter in line:
      a.append(letter)
    if not a==[]:
      lines.append(a)
  return lines

def checkStatus(r0, r1, r2, r3):
  rowsOrig=[r0,r1,r2,r3]
  r0n=r0[:]
  r1n=r1[:]
  r2n=r2[:]
  r3n=r3[:]
  rows=[r0n,r1n,r2n,r3n]
  
  for row in rows:
    if 'T' in row:
      row.remove('T')
      if (row[0]==row[1]==row[2])and(row[0]!='.'):
	return (str(row[0])+" won")
    elif (row[0]==row[1]==row[2]==row[3])and(row[0]!='.'):
      return (str(row[0])+" won")
  
  for i in range(4):
    r0n=r0[:]
    r1n=r1[:]
    r2n=r2[:]
    r3n=r3[:]
    rows=[r0n,r1n,r2n,r3n]
    column=[rows[0][i],rows[1][i],rows[2][i],rows[3][i]]
    if 'T' in column:
      column.remove('T')
      if (column[0]==column[1]==column[2])and(column[0]!='.'):
	return (str(column[0])+" won")
    elif (column[0]==column[1]==column[2]==column[3])and(column[0]!='.'):
      return (str(column[0])+" won")
  
  r0n=r0[:]
  r1n=r1[:]
  r2n=r2[:]
  r3n=r3[:]
  rows=[r0n,r1n,r2n,r3n]
  diag1=[rows[0][0],rows[1][1],rows[2][2],rows[3][3]]
  if 'T' in diag1:
      diag1.remove('T')
      if (diag1[0]==diag1[1]==diag1[2])and(diag1[0]!='.'):
	return (str(diag1[0])+" won")
  elif (diag1[0]==diag1[1]==diag1[2]==diag1[3])and(diag1[0]!='.'):
      return (str(diag1[0])+" won")
  
  r0n=r0[:]
  r1n=r1[:]
  r2n=r2[:]
  r3n=r3[:]
  rows=[r0n,r1n,r2n,r3n]
  diag2=[rows[0][3],rows[1][2],rows[2][1],rows[3][0]]
  if 'T' in diag2:
      diag2.remove('T')
      if (diag2[0]==diag2[1]==diag2[2])and(diag2[0]!='.'):
	return (str(diag2[0])+" won")
  elif (diag2[0]==diag2[1]==diag2[2]==diag2[3])and(diag2[0]!='.'):
      return (str(diag2[0])+" won")
  for row in rows:
    if '.' in row:
      return 'Game has not completed'
  return 'Draw'

lines=readFile()
x=int("".join(lines[0])) #x is number of cases
lines.remove(lines[0]) #now lines is list of lists
y=0
file1=open('outputLarge','w') #make a blank file
for i in range(x):
  output= 'Case #'+str(i+1)+': '+checkStatus(lines[y],lines[y+1],lines[y+2],lines[y+3])
  print output
  file1=open('outputLarge','a') #open file
  file1.write(output+'\n') #write to file
  file1.close()            #close the file
  y=y+4
