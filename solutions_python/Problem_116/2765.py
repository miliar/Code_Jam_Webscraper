#!/usr/bin/python
import re
filePrefix = 'A-small-attempt0'
fin = open(filePrefix + '.in', 'r')
fout = open(filePrefix + '.out', 'w')
T = int(fin.readline())

def answer(array):
    xmatch = re.search(r'[XT][XT][XT][XT]',array)
    omatch = re.search(r'[OT][OT][OT][OT]',array)
    xmatch_diag1 = re.search(r'[XT][\w\.][\w\.][\w\.][\w\.][XT][\w\.][\w\.][\w\.][\w\.][XT][\w\.][\w\.][\w\.][\w\.][XT]',array)
    omatch_diag1 = re.search(r'[OT][\w\.][\w\.][\w\.][\w\.][OT][\w\.][\w\.][\w\.][\w\.][OT][\w\.][\w\.][\w\.][\w\.][OT]',array)
    xmatch_diag2 = re.search(r'[\w\.][\w\.][\w\.][XT][\w\.][\w\.][XT][\w\.][\w\.][XT][\w\.][\w\.][XT][\w\.][\w\.][\w\.]',array)
    omatch_diag2 = re.search(r'[\w\.][\w\.][\w\.][OT][\w\.][\w\.][OT][\w\.][\w\.][OT][\w\.][\w\.][OT][\w\.][\w\.][\w\.]',array)
    xmatch_vert = re.search(r'[XT][\w\.][\w\.][\w\.][XT][\w\.][\w\.][\w\.][XT][\w\.][\w\.][\w\.][XT]',array)
    omatch_vert = re.search(r'[OT][\w\.][\w\.][\w\.][OT][\w\.][\w\.][\w\.][OT][\w\.][\w\.][\w\.][OT]',array)
    if xmatch:
      print xmatch.start()
    print xmatch_diag1
    print xmatch_diag2
    if xmatch:
      if xmatch.start() % 4 == 0:
          return "X won"
    if omatch:
      if omatch.start() % 4 == 0:
        return "O won"
    if xmatch_diag1 or xmatch_diag2 or xmatch_vert:
      return "X won"
    if omatch_diag1 or omatch_diag2 or omatch_vert:
      return "O won"
    if "." in array:
      return "Game has not completed"
    return "Draw"

for i in range(T):
  array = ''
  array = array + fin.readline().strip()
  array = array + fin.readline().strip()
  array = array + fin.readline().strip()
  array = array + fin.readline().strip()
  fin.readline().strip() 
  fout.write("Case #%d: %s\n" % ((i+1), answer(array)))
#print(sorted(list(code_dict.values())))
