##
##  Code Jam 2013 Problem 1
##  chang.liu@jhu.edu
##

# A function
def check(rows, cols, x, i):
  #check each line
  for line in rows:
    if(('X' in line) and ('O' not in line) and ('.' not in line)):
      out.write('Case #' + str(i) + ': X won\n')
      return
    if(('O' in line) and ('X' not in line) and ('.' not in line)):
      out.write('Case #' + str(i) + ': O won\n')
      return
      
  #check each col
  for col in cols:
    if(('X' in col) and ('O' not in col) and ('.' not in col)):
      out.write('Case #' + str(i) + ': X won\n')
      return
    if(('O' in col) and ('X' not in col) and ('.' not in col)):
      out.write('Case #' + str(i) + ': O won\n')
      return
      
  # check X
  for eachx in x:
    if(('X' in eachx) and ('O' not in eachx) and ('.' not in eachx)):
      out.write('Case #' + str(i) + ': X won\n')
      return
    if(('O' in eachx) and ('X' not in eachx) and ('.' not in eachx)):
      out.write('Case #' + str(i) + ': O won\n')
      return
  
  # check incomplete game
  for line in rows:
    if('.' in line):
      out.write('Case #' + str(i) + ': Game has not completed\n')
      return
      
  out.write('Case #' + str(i) + ': Draw\n')
  return

fp = open("A-large.in", "r")
out = open('A-large.out', 'w')
n = int(fp.readline())
# END of this function


# init vectors
for i in range(n):
  rows = []
  cols = []
  x = []
  
  line1 = fp.readline()[:-1]
  line2 = fp.readline()[:-1]
  line3 = fp.readline()[:-1]
  line4 = fp.readline()[:-1]
  # generate row
  rows.append(line1)
  rows.append(line2)
  rows.append(line3)
  rows.append(line4)
  
  # generate col
  for c in range(4):
    tmpcol = []
    tmpcol.append(line1[c])
    tmpcol.append(line2[c])
    tmpcol.append(line3[c])
    tmpcol.append(line4[c])
    tmpcol = ''.join(tmpcol)
    cols.append(tmpcol)
  
  # generate X
  tmpx = []
  tmpx.append(line1[0])
  tmpx.append(line2[1])
  tmpx.append(line3[2])
  tmpx.append(line4[3])
  tmpx = ''.join(tmpx)
  x.append(tmpx)
  tmpx = []
  tmpx.append(line1[3])
  tmpx.append(line2[2])
  tmpx.append(line3[1])
  tmpx.append(line4[0])
  tmpx = ''.join(tmpx)
  x.append(tmpx)
  
  fp.readline() # line 5 - Empty line
  
  check(rows, cols, x, i+1)


