import sys
T = int(sys.stdin.readline())
for t in range(T):
  C,F,X = map(float, sys.stdin.readline().split())
  cps = 2.0
  res = 0.0
  derecho = 1 
  nuevo_tiempo = 0
  # import pudb;pu.db
  while nuevo_tiempo < derecho:
    tiempo_compra = C / cps
    derecho = X / cps 
    nuevo_tiempo = tiempo_compra + (X/ (cps + F))

    if nuevo_tiempo < derecho:
      res += tiempo_compra
      cps = cps + F
  res += derecho

  print 'Case #' + str(t+1) + ':', res
