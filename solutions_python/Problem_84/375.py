I,O=open('test.txt','rU'),open('output.txt','w')
W,R=O.write,I.readline

for main in range(int(R())):
  ts = []
  d = map(int,R().split(' '))
  for i in range(d[0]): ts += [list(R())]
  for i in range(d[0]-1):
    for j in range(d[1]-1):
      if ts[i][j]==ts[i+1][j]==ts[i][j+1]==ts[i+1][j+1]=='#': ts[i][j],ts[i+1][j],ts[i][j+1],ts[i+1][j+1]='/','\\','\\','/'
  W('Case #%d:\n'%(main+1))
  for k in ts:
    if '#' in k:
      W('Impossible\n')
      break
  else:
    for r in ts: W(''.join(r))

I.close()
O.close()