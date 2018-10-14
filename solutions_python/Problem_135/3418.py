'''
Created on Apr 12, 2014

@author: richard
'''

from collections import defaultdict

def buildGrid(grid_str):
  
  grid = []
  for row in range(0,len(grid_str)):
    grid.append([])
    for val in grid_str[row].split():
      grid[row].append(val)
  return grid

def parseCase(lines):
  sRow1 = lines[0]
  grid1 = buildGrid(lines[1:5])
#   print(lines[1:5])
#   print grid1,sRow1
  sRow2 = lines[5]
#   print(lines[6:11])
  grid2 = buildGrid(lines[6:])
#   print grid2, sRow2
  return (sRow1, grid1, sRow2, grid2)

def findCard(nrow1, arrg1, nrow2, arrg2):
  
#   print len(arrg1)
#   print (nrow1, nrow2)
  row1 = set(arrg1[nrow1])
  row2 = set(arrg2[nrow2])
  return list(row1.intersection(row2))
  
if __name__ == '__main__':
  
  import sys
  
  fileName = sys.argv[1]
  file = open(fileName)
  lines = file.readlines()
  nCases = int(lines[0])
  start = 1
  for c in range(1,nCases+1):
    
    end = start+10
    (sRow1, grid1, sRow2, grid2) = parseCase(lines[start:end])
    res = findCard(int(sRow1)-1, grid1, int(sRow2)-1, grid2)
    if len(res) == 1:
      print 'case #%d: %s  '%(c, res[0])
    elif len(res) > 1:
      print 'case #%d: Bad magician!'%c
    else:
      print 'case #%d: Volunteer cheated!'%c
    start = end