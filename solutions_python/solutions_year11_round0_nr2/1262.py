#!/usr/bin/python

import sys

def printOutput(case, elems):
  print "Case #" + str(case) + ": [" + ", ".join(elems) + "]" 

def processFile(filename):

  f = open(filename)

  T = int(f.readline().strip('\n'))

  count = 0

  while count < T:

    Case = f.readline().strip('\n').split(' ')
    
    C = int (Case[0])
    del Case[0]

    CList = []
    for val in Case[:C]:
      CList.extend(list(val))
    del Case[:C]

    D = int(Case[0])
    del Case[0]
 
    DList = "".join(Case[:D])
    del Case[:D]

    N = int(Case[0])
    del Case[0]

    NList = []
    for val in Case[:N]:
      NList.extend(list(val))
    del Case[:N]

    Elems = playMagicka(CList, DList, NList)  

    printOutput(count+1, Elems)

    count += 1

def playMagicka(CList, DList, NList):

  Elems = []
  index = 0

  if len(CList) > 2 and CList[0] == CList[1]:
    CList_has_same = True
  else:
    CList_has_same = False

  for letter in NList:
  
    if len(Elems) == 0:
      Elems.insert(index, letter)
      index += 1
      continue
  
    prev_letter = Elems[index-1]
    
    if letter == prev_letter:
      same_as_prev = True
    else:
      same_as_prev = False

    if letter in CList and prev_letter in CList[:2]:
      
      if same_as_prev and not CList_has_same:
        Elems.insert(index, letter)
        index += 1
        continue
      
      Elems.pop()
      Elems.insert(index-1, CList[2])
      continue

    elif letter in DList and DList.replace(letter, '') in Elems:
      Elems = []
      index = 0
      continue
    
    Elems.insert(index, letter)
    index += 1  
  
  return Elems

def main():

  args = sys.argv[1:]
  processFile(args[0])

if __name__ == '__main__':
  main()
