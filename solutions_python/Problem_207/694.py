
import sys 

def unicornSmall(N, colors):
  R = int(colors[0])
  Y = int(colors[2])
  B = int(colors[4])
  if R>Y+B or Y>B+R or B>Y+R:
    print("IMPOSSIBLE")
    return(False)
  y = ['R', 'Y', 'B']
  x = []
  x.append([R, 0])
  x.append([Y, 1])
  x.append([B, 2])
  x.sort()
  counter = N
  triplets = x[0][0] - (x[2][0] - x[1][0])
  x[0][0] -= triplets
  x[1][0] -= triplets
  x[2][0] -= triplets
  counter -= (3*triplets)
  while triplets > 0:
    print(y[x[2][1]], y[x[1][1]], y[x[0][1]], sep='', end='')
    triplets -= 1
  duplets = x[1][0]
  counter -= (2*duplets)
  x[1][0] -= duplets
  x[2][0] -= duplets
  while duplets > 0:
    print(y[x[2][1]], y[x[1][1]], sep='', end='')
    duplets -= 1    
  duplets = x[0][0]
  x[0][0] -= duplets
  x[2][0] -= duplets
  while duplets > 0:
    print(y[x[2][1]], y[x[0][1]], sep='', end='')
    duplets -= 1     
  print("")
  return(counter)

def readFile(inputFile):
  with open(inputFile) as infile:
    num = 1
    numCases = int(infile.readline().rstrip())
    while num <= numCases:
      line = infile.readline()
      line = line.rstrip()      
      columns = line.split()
      N = int(columns[0])
      colors = columns[1:]
      print('Case #', num, ': ', sep='', end='')
      res = unicornSmall(N, colors)
      num += 1

if __name__ == "__main__":
  inputFile = sys.argv[1]
  readFile(inputFile)

