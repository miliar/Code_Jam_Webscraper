import sys 
import string

f = open(sys.argv[1])

T = int(f.readline())
for c in xrange(0, T): 
  L = [[] for i in range(4)]
  H = [[] for i in range(4)]
  L[0] = f.readline()
  L[1] = f.readline()
  L[2] = f.readline()
  L[3] = f.readline()
  f.readline()
  #strings has all the horizontal strings, now add all the vertical strings
  H[0] = ''.join(L[i][0] for  i in range(4))
  H[1] = ''.join(L[i][1] for  i in range(4))
  H[2] = ''.join(L[i][2] for  i in range(4))
  H[3] = ''.join(L[i][3] for  i in range(4))
  D1 = ''.join(L[i][i] for i in range(4))
  D2 = ''.join((L[3][0], L[2][1], L[1][2], L[0][3]))
  strings = list()
  for i in range(4):
    strings.append(H[i].strip())
    strings.append(L[i].strip())
  strings.append(D1)
  strings.append(D2)
  stringx = list()
  stringso = list()
  dots = 0
  for st in strings:
    if '.' in st:
      dots+=1
    stringx.append(st.replace('T', 'X'))
    stringso.append(st.replace('T', 'O'))
  #print stringx
  #print stringso
  if 'XXXX' in stringx: 
    print ''.join(('Case #', str(c+1), ': X won'))
  elif 'OOOO' in stringso:
    print ''.join(('Case #', str(c+1), ': O won'))
  elif dots>0:
    print ''.join(('Case #', str(c+1), ': Game has not completed'))
  else:
    print ''.join(('Case #', str(c+1), ': Draw'))
