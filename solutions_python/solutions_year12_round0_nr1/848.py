import os
import sys


def getKnowledge():
  knowledge = {}
  fG = file('googler.txt','rU')
  fE = file('english.txt','rU')
  linesG = fG.readlines()
  linesE = fE.readlines()
  for i in range(len(linesG)):
    for j in range(len(linesG[i])):
      knowledge[linesG[i][j]] = linesE[i][j]
  fG.close()
  fE.close()
  knowledge['z'] = 'q'
  return knowledge

def getInput(pathToI):
  f = file(pathToI)
  lines = f.readlines()
  rge = range(len(lines))[1:]
  sentences = []
  for i in rge:
    sentences.append(lines[i])
  f.close()
  return sentences

def translate(sentences,kn):
  trans = []
  for line in sentences:
    lineTrans = ""
    for i in range(len(line)):
      lineTrans += kn[line[i]]
    trans.append(lineTrans)
  return trans

def printSol(trans, path):
  w = file(path,'w')
  i = 1
  for line in trans:
    w.write("Case #")
    w.write(str(i))
    w.write(": ")
    i+=1
    w.write(line)
  w.close()

def main():
  kn = getKnowledge()
  args = sys.argv[1:]
  sentences = getInput(args[0])
  trans = translate(sentences,kn)
  printSol(trans,args[1])
  print trans

main()

