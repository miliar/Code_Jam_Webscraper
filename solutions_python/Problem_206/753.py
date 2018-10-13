
import sys 

def bestSpeed(horses, N, D):
  km = horses[0][0]
  speed = horses[0][1]
  latest = (D - km)/speed
  for rider in horses:
    km = rider[0]
    speed = rider[1]
    hours = (D - km)/speed
    if hours > latest:
      latest = hours
  annie = D/latest
  return(annie)

def readFile(inputFile):
  with open(inputFile) as infile:
    num = 1
    numCases = int(infile.readline().rstrip())
    while num <= numCases:
      horses = []
      line = infile.readline()
      line = line.rstrip()      
      DN = line.split()
      D = int(DN[0]) # destination
      N = int(DN[1]) # other horses
      for i in range(N):
        line = infile.readline()
        line = line.rstrip()
        columns = line.split()
        km = int(columns[0])
        speed = int(columns[1])
        horses.append((km, speed))
      res = bestSpeed(horses, N, D)
      print('Case #', num, ': ', res, sep='')
      num += 1

if __name__ == "__main__":
  inputFile = sys.argv[1]
  readFile(inputFile)

