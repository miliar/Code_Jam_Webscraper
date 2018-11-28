def contieneTodos(arreQueries,arreBuscadores):
  setQueries=set(arreQueries)
  setBuscadores=set(arreBuscadores)
  return setQueries.issuperset(setBuscadores)

def buscaMenos(arreQueries):
  i = len(arreQueries) - 1
  while (i >= 0 ):
    item = arreQueries[i]
    j= i-1;
    while (j>=0):
      if (item == arreQueries[j]):
        break
      j=j-1
    if (j==-1):
      return i
    i=i-1

f=open('./A-large.in', 'r')
casos = f.readline()
for iCasos in range(int(casos)):
  buscadores = f.readline()
  arreBuscadores = range(int(buscadores))
  for iBuscadores in range(int(buscadores)):
    arreBuscadores[iBuscadores] = f.readline().strip()
  queries = f.readline()
  arreQueries = range(int(queries))
  for iQueries in range(int(queries)):
    arreQueries[iQueries] = f.readline().strip()
  menos= len(arreQueries)
  suma=0
  while (True):
    if (contieneTodos(arreQueries,arreBuscadores)):
      menos = buscaMenos(arreQueries)
      arreQueries = arreQueries[menos:]
      suma=suma+1
    else:
      #print "termino"
      break

  print "Case #"+str(iCasos+1)+":",suma