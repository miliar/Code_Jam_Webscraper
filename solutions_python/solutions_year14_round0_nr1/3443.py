import sys

with open(sys.argv[1], 'r') as inp, open(sys.argv[2], 'w') as outp:
  casos = int(inp.readline())
  for i in range(casos):
    posibles = range(1,17)
    for j in range(2):
      row = int(inp.readline()) - 1
      tabla = [map(int, inp.readline().split()) for k in range(4)]
      posibles = [x for x in posibles if x in tabla[row]]
    outp.write("Case #%d: " % (i + 1))
    if len(posibles) == 0:
      outp.write("Volunteer cheated!\n")
    elif len(posibles) > 1:
      outp.write("Bad magician!\n")
    else:
      outp.write(str(posibles[0]) + "\n")
