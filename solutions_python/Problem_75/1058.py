I,O=open('test.txt','rU'),open('output.txt','w')
W,R=O.write,I.readline
for main in range(int(R())):
  line,comb,opp = R().split(' '),{},[]
  C = int(line[0])
  if C:
    for i in range(C):
      s = line[i+1]
      comb[s[:2]] = comb[s[:2][::-1]] = s[2]
  D = int(line[1+C])
  if D:
    for i in range(D): opp += [line[i+2+C]]
  queue = [c for c in line[-1]]
  list = []
  for E in queue:
    list += E
    try:
      p = list[-2]+list[-1]
      if p in comb: 
        list[-2:] = comb[p]
      for i in opp:
        if E in i:
          if i[0] in list and i[1] in list: list = []
    except: pass
  final = '['+', '.join(list[:-1])+']'
  W('Case #%d: %s\n'%(main+1,final))
  print 'Case #%d: %s\n'%(main+1,final)
I.close()
O.close()