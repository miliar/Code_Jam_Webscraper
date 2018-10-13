#!/usr/bin/python
import os,io,math,sys

def run(filename):

  fair=[]
  fin = open(filename, 'r')
  fout = open('output.out','w')
  T = int(fin.readline())
  
  for i in range(1,10000001):
    if checkPalindrom(i) and checkPalindrom(i*i):
      fair.append(i*i)
 
  print 'fairs are ready'
  for t in range(T):
    # read
    [A,B]=fin.readline().split(" ")
    A = int(A)
    B = int(B)

    # solve
    res = 0
    for sp in fair:
      if sp >= A and sp <= B:
        res += 1


    # write
    fout.write("Case #%d: %d\n" %(t+1,res) )
    print 'Res:',res

  fin.close()
  fout.close()

def checkPalindrom(p):
  sp = str(p)
  for i in range(len(sp)/2):
    if sp[i] != sp[-i-1]:
     return False
  return True

if __name__ == "__main__":
  run(sys.argv[1])
