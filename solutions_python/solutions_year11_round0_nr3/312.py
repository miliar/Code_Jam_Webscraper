cant = int(raw_input())
for t in range(cant):
  cant = int(raw_input())
  valstrs = raw_input().split(' ')
  enteros = []
  sepuede = 0
  for val in valstrs:
    valor = int(val)
    sepuede = sepuede ^ valor
    enteros.append(int(val))

  if sepuede != 0:
    print "Case #{0}: NO".format(t+1)
  else: 
    minimo = 1000000000 
    for val in enteros:
      if val < minimo and val > 0:
        minimo = val
    suma = 0
    yapaso = False
    for val in enteros:
      if val != minimo or yapaso:
        suma += val
      else:
        yapaso = True 
    print "Case #{0}: {1}".format(t+1, suma)
  
