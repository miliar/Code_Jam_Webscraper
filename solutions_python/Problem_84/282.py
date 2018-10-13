#!/usr/bin/python -tt

import sys
import fractions

def doWork(case): 
  for i, line in enumerate(case): 
    for j, element in enumerate(line):
      if element == ".": 
        continue
      if element == "#": 
        try:
          if case[i][j+1] == element and case[i+1][j] == element and case[i+1][j+1] == element:
            case[i][j] = '/'
            case[i+1][j] = '\\'
            case[i][j+1] = '\\'
            case[i+1][j+1] = '/'
          else: 
            return False
        except IndexError:
          return False
  return case
  

def main():
  f = open("input", 'rU')
  lines = f.readline()
  #output = open('output', 'w')
  for i in range(int(lines)):
    #line = f.readline().split(" ")
    #a, b, c = map(int, line)
    #line = f.readline().split())
    case = []
    for j in range(int(f.readline().split()[0])):
      case.append(list(f.readline())[:-1])
    #print case
    answer = doWork(case)
    if answer: 
      print ("Case #%d:" % (i+1))
      for j in case:
        print ''.join(j)
    else:
      print ("Case #%d:\nImpossible" % (i+1))
    #print input
    #answer = doWork(a, b, c)
    #answer = doWork(int(line[0]), int(line[1]), int(line[2]))
    #print ("Case #%d: %s" % (i+1, answer)
    #print ("Case #%d:" % (i+1))
    #output.write("Case #%d: %s\n" % (i+1, answer))
  f.close()
  #output.close()
  
if __name__ == '__main__':
  main()
