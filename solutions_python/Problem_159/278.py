IN = open("in", 'r')
OUT = open("out", 'w')

t = IN.readline()


for x in xrange(1, int(t) + 1):
  N = int(IN.readline())
  M = map(int, IN.readline().strip().split(' ')) 
  
  maxT = 0
  suma = 0
  suma2 = 0
  
  for i in xrange(0,N-1):
    difT = M[i]-M[i+1]
    if difT > 0:
      suma += difT
    if difT > maxT:
      maxT = difT  

  for i in xrange(0,N-1):
    if M[i] > maxT:
      suma2 += maxT
    else:
      suma2 += M[i]


  outline = "Case #" + str(x) + ": " + str(suma) + " " + str(suma2) + "\n"
  print outline
  OUT.write(outline)


OUT.close()
IN.close()