cant = int(raw_input())
for t in range(cant):
  texto = raw_input().split(' ')
  cb = int(texto[0])
  camino = texto[1:]
  actual = camino[0] 
  pos = { 'O': 1, 'B': 1 }
  segundos = 0
  segse = 0
  for i in range(cb):
    letra = camino[i*2]
    boton = int(camino[i*2+1])
    if actual != letra:
      mov = abs(boton - pos[letra]) - segse
      if mov < 0:
        mov = 0
      segse = mov + 1
    else:
      mov = abs(boton - pos[letra])
      segse += mov + 1
    segundos += mov + 1
    pos[letra] = boton
    actual = letra

  print "Case #{0}: {1}".format(t+1, segundos)
