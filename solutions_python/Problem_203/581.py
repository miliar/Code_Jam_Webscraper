import math

def fillR(cake, r, c):
  for i in range(r):
    for j in range(1, c):
      if cake[i][j] == '?':
        cake[i][j] = cake[i][j - 1]

def fillL(cake, r, c):
  for i in range(r):
    for j in range(c - 2, -1, -1):
      if cake[i][j] == '?':
        cake[i][j] = cake[i][j + 1]

def fillD(cake, r, c):
  for i in range(1, r):
    for j in range(c):
      if cake[i][j] == '?':
        cake[i][j] = cake[i - 1][j]

def fillU(cake, r, c):
  for i in range(r - 2, -1, -1):
    for j in range(c):
      if cake[i][j] == '?':
        cake[i][j] = cake[i + 1][j]

def printCake(cake, r, c):
  for i in range(r):
    print ''.join(cake[i])

if __name__ == '__main__':
  noTestCases = int(raw_input())
  for testCaseNo in range(1, noTestCases + 1):
    r, c = map(int, raw_input().strip().split(' '))
    cake = []
    for ri in range(r):
      cake.append(list(raw_input().strip()))
    fillR(cake, r, c)
    fillL(cake, r, c)
    fillD(cake, r, c)
    fillU(cake, r, c)
    print 'Case #' + str(testCaseNo) + ': '
    printCake(cake, r, c)