import sys
def solveline(line):
  if not "." in line:
    T = line.find('T')
    if T > 0:
      sline = list(line)
      sline[T] = line[(T+1)%4]
      line = "".join(sline)
    if line == "XXXX":#['X','X','X','X']:
      print "X won"
      return True
    if line == "OOOO":#['O','O','O','O']:
      print "O won"
      return True
  return False

if __name__ == "__main__":
  f = sys.stdin
  if len(sys.argv) >= 2:
    fn = sys.argv[1]
    f = open(fn, 'r')
  num = int(f.readline())
  for i in range(num):
    sys.stdout.write ("Case #"+str(i + 1)+": ")
    solved = False
    finished = True
    v1=[]
    v2=[]
    v3=[]
    v4=[]
    d1=[]
    d2=[]
    for j in range(4):
      line = f.readline()
      solved = solved or solveline(line[0:-1])
      if not solved:
        finished = finished and not "." in line
        v1.append(line[0])
        v2.append(line[1])
        v3.append(line[2])
        v4.append(line[3])
        d1.append(line[j])
        d2.append(line[3-j])
    if not solved:
      solved = solved or solveline("".join(v1))
      solved = solved or solveline("".join(v2))
      solved = solved or solveline("".join(v3))
      solved = solved or solveline("".join(v4))
      solved = solved or solveline("".join(d1))
      solved = solved or solveline("".join(d2))
      if not solved:
        if not finished:
          print "Game has not completed"
        else:
          print "Draw"
    f.readline() #read last newline
