attempt_list = ["A-test","A-small-attempt0","A-large"]
attempt = attempt_list[2]

import time
time.clock()

def solve1(n, plate):
  totalmush = 0
  for i in range(n-1):
    totalmush += max(plate[i]-plate[i+1],0)
  return str(totalmush)

def solve2(n, plate):
  maxmush = 0
  for i in range(n-1):
    maxmush = max(maxmush, plate[i]-plate[i+1])
  totalmush = 0
  for i in range(n-1):
    totalmush += min(plate[i],maxmush)
  return str(totalmush)

def main():
  fin = open(attempt + ".in", 'r')
  fout = open(attempt + ".out",'w')

  numcases = int(fin.readline())

  for casenum in range(1,numcases+1):
    n = int(fin.readline())
    plate = map(int, fin.readline().split())
    fout.write('Case #' + repr(casenum) + ': ' + solve1(n, plate) + " " + solve2(n, plate) + "\n")

  fin.close()
  fout.close()

main()
print(time.clock())