#!/usr/bin/python
import os,io,math,sys

def run(filename):

  fin = open(filename, 'r')
  fout = open('output.out','w')
  T = int(fin.readline())
  for t in range(T):
    # read
    ttt = []
    for i in range(4):
      line = fin.readline()
      ttt.append(line)
    if t<T:
      fin.readline()
    print "Read done",t

    # solve
    res = None
    # horizontal
    if res == None:
      for line in ttt:
        res = whoWin(line)
        if res != None:
          break

    # vertical
    if res == None:
      for i in range(4):
        line = [ttt[0][i], ttt[1][i], ttt[2][i], ttt[3][i]]
        res = whoWin(line)
        if res != None:
          break

    # diagonal
    if res == None:
      line = [ttt[0][0], ttt[1][1], ttt[2][2], ttt[3][3]]
      res = whoWin(line)
    if res == None:
      line = [ttt[3][0], ttt[2][1], ttt[1][2], ttt[0][3]]
      res = whoWin(line)

    finished = True
    for line in ttt:
      for p in line:
        if p == '.':
          finished = False
          break
      if not finished:
        break

    # write
    if res == 'X':
      fout.write("Case #%d: X won\n" %(t+1))
    elif res == 'O':
      fout.write("Case #%d: O won\n" %(t+1))
    elif not finished:
      fout.write("Case #%d: Game has not completed\n" %(t+1))
    else:
      fout.write("Case #%d: Draw\n" %(t+1))
 
  fin.close()
  fout.close()

# X, O, None
def whoWin(line):
  win = ''
  countT = 0
  for t in line[0:4]:
    if t == "T":
      countT += 1
    elif t == '.':
      return None
    elif win == '':
      win = t
    elif win != t:
      return  None
      
  return win if countT <= 1 else None

if __name__ == "__main__":
  run(sys.argv[1])
