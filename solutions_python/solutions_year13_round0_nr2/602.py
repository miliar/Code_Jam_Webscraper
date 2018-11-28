import sys, os

_debug_ = False

if 'debug' in sys.argv:
 _debug_ = True

def log(mesg,newline=True):
 if _debug_:
  print mesg,
  if newline: print

lines = sys.stdin.read().strip().split("\n")

numcases = int(lines.pop(0))
case=0

while case<numcases:
  case+=1
  matrix=[]
  rowmax=[]
  colmax=[]
  #log(lines[0])
  m,n = ( int(v) for v in lines.pop(0).split())
  for i in range(0,m):
    rowvalues = [ float(v) for v in lines.pop(0).split() ]
    matrix.append(rowvalues )
    rowmax.append(max(rowvalues))
  for i in range(0,n):
    #calculate colmax, trick didnt work :(
    colmax.append(max( v[i] for v in matrix))
  #colmax=map(max,matrix)		#awesome trick :) didnt work
  for i in range(0,m):
    for j in range(0,n):
      log( matrix[i][j] , False)
    log(": %d"%rowmax[i])
  log(colmax)

  #start the check for the case here:
  result=True
  for i in range(0,m):
    for j in range(0,n):
      if rowmax[i] > matrix[i][j] and  colmax[j] > matrix[i][j]:
        print "Case #%d: NO"%case
        log("case fails for %d,%d with value %f, rowmax = %f, colmax = %f"%(i,j,matrix[i][j], rowmax[i], colmax[j]))
        result=False
        break
    if not result: break
  if result: print "Case #%d: YES"%case


