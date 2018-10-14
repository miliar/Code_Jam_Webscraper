def main():
  fi = open('Input.txt')
  fo = open('Output.txt','w')
  T = int(fi.readline())
  answer=""
  for j in xrange(T):
    list = []
    for i in xrange(4):
      list.append(fi.readline().strip())
    fi.readline()

    winCount=[0,0,0,0]
    H = checkHorizontal(list)
    V = checkVertical(list)
    R = checkLeftDiagonal(list)  
    L = checkRightDiagonal(list)  
    if H=="X won" or V=="X won" or R=="X won" or L=="X won" :
      winCount[0]+=1
    elif H=="O won" or V=="O won" or R=="O won"or L=="O won" :
      winCount [1]+=1
    elif H=="Draw" or V=="Draw" or R=="Draw" or L=="Draw" :
      winCount[2]+=1

    if winCount[0] == 1:
      answer= "X won"
    elif winCount [1] ==1:
      answer="O won"
    elif winCount [2] ==1:
      answer="Draw"
    else:
      answer="Game has not completed"
    fo.write('Case #' +str(j+1)+ ':'+" "+answer+"\n")
  fi.close()
  fo.close()
def checkHorizontal(list):
  answer="Game has not completed"
  for i in xrange(4):
    xCount=0
    oCount=0
    empty = False
    for j in xrange(4):
      if list[i][j] == "X":
        xCount+=1
      if list[i][j] == "O":
        oCount+=1
      if list[i][j] == "T":
        xCount+=1
        oCount+=1
      elif list[i][j] == ".":
        empty = True
    if xCount == 4:
      answer = "X won"
      break
    elif oCount == 4:
      answer = "O won"
      break
    elif empty == False:
      answer = "Draw"
    else:
      answer = "Game has not completed"
  return answer
def checkVertical(list):
  answer = "Game has not completed"
  for i in xrange(4):
    xCount=0
    oCount=0
    empty = False
    for j in xrange(4):
      if list[j][i] == "X":
        xCount+=1
      if list[j][i] == "O":
        oCount+=1
      if list[j][i] == "T":
        xCount+=1
        oCount+=1
      elif list[j][i] == ".":
        empty = True
    if xCount == 4:
      answer = "X won"
      break
    elif oCount == 4:
      answer = "O won"
      break
    elif empty == False:
      answer = "Draw"
    else:
      answer = "Game has not completed"
  return answer

def checkLeftDiagonal(list):
  answer = "Game has not completed"
  xCount=0
  oCount=0
  empty = False
  for i in xrange(4):
    if list[i][i] == "X":
      xCount+=1
    if list[i][i] == "O":
      oCount+=1
    if list[i][i] == "T":
      xCount+=1
      oCount+=1
    elif list[i][i] == ".":
        empty = True
    if xCount == 4:
      answer = "X won"
      break
    elif oCount == 4:
      answer = "O won"
      break
    elif empty == False:
      answer = "Draw"
    else:
      answer = "Game has not completed"
  return answer

def checkRightDiagonal(list):
  answer = "Game has not completed"
  xCount=0
  oCount=0
  empty = False
  count=-1
  for i in xrange(3,-1,-1):
    count+=1
    if list[count][i] == "X":
      xCount+=1
    if list[count][i] == "O":
      oCount+=1
    if list[count][i] == "T":
      xCount+=1
      oCount+=1
    elif list[count][i] == ".":
        empty = True
    if xCount == 4:
      answer = "X won"
      break
    elif oCount == 4:
      answer = "O won"
      break
    elif empty == False:
      answer = "Draw"
    else:
      answer = "Game has not completed"
  return answer
main()
