import sys

def isChange(tripete, izq, der):
  if tripete[0] == izq and tripete[1] == der:
    return True
  
  if tripete[1] == izq and tripete[0] == der:
     return True
  
  return False

cant = int(raw_input())
for t in range(cant):
  texto = raw_input().split(' ')
  ts = int(texto[0])
  tripetes = texto[1:1+ts]   
  os = int(texto[1+ts])
  opuestos = texto[ts+2:ts+2+os]
  largo = int(texto[ts+2+os])
  entrada = texto[ts+3+os]
  
  final = []
  for i in range(largo):
    final.append(entrada[i])
    lf = len(final)
    if lf == 1:
      continue
    added = False
    for trip in tripetes:
      if isChange(trip, final[lf-2], final[lf-1]):
        final.pop()
        final.pop()
        final.append(trip[2])
        added = True
        break
    if added:
      continue
    
    clean = False
    for dup in opuestos:
      for ele in final:
        if dup[0] == final[lf-1] and dup[1] == ele:
          clean = True
          break
        if dup[1] == final[lf-1] and dup[0] == ele:
          clean = True
          break
      if clean:
        break
    if clean:
      final = [] 
          
  sys.stdout.write( "Case #{0}: [".format(t+1))
  if len(final) > 0:
    sys.stdout.write( final[0])
    for val in final[1:]:
      sys.stdout.write(", {0}".format(val))
  sys.stdout.write( "]")
  print ''         
