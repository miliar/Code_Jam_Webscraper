import sys

filename = sys.argv[1]

infile = open(filename)

T = int(infile.readline())

for x in range(T):
  sys.stdout.write("Case #")
  sys.stdout.write(str(x+1))
  sys.stdout.write(": ")
  
  params = infile.readline().split()
  N = int(params[0])
  K = int(params[1])
  
  x = 1
  for i in range(N-1):
    x <<= 1
    x += 1
    
  if ((K & x) == x):
    print "ON"
  else:
    print "OFF"

infile.close()