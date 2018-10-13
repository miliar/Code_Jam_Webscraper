#!/usr/bin/env python2

from math import *

# remove duplicates
def f7(seq):
   seen = set()
   seen_add = seen.add
   return [ x for x in seq if x not in seen and not seen_add(x)]

def findPal(digitNb):

   res = []

   print "palindrome a digit = " + str(digitNb)
   print "iteration de 0 a " + str(int(pow(10, ceil(float(digitNb)/2))))

   for i in range(int(pow(10, ceil(float(digitNb)/2)))):

      if digitNb % 2 == 0:
         res.append(int(str(i) + str(i)[::-1]))
      else:
         inv = str(i)[::-1]
         res.append(int(str(i) + inv[:-1] ))

   #print "nb sols = " + str(len(res))
   return res

def solve(itrv):

   res = 0
   openSols = []
   openSols2 = []

   #print itrv
   sqrtItrv = [int(ceil(sqrt(itrv[0]))), int(sqrt(itrv[1]))]
   #print sqrtItrv

   d = 0
   while pow(10, d) <= sqrtItrv[1]:
      d += 1
      openSols += findPal(d)

   #print "nb total sols = " + str(len(openSols))

   for s in openSols:
      #print s
      if s >= sqrtItrv[0] and s <= sqrtItrv[1]:
         #print "ajout"
         openSols2.append(s)

   #print "nb total sols dans interval = " + str(len(openSols2))

   openSols2 = f7(openSols2)
   for s in openSols2:
      c = str(s*s);
      if c == c[::-1]:
         res += 1

   return res

def main():

   intervals = []

   with open('C-small.in') as fileIn:
      gameNb = int(fileIn.readline())

      for game in range(gameNb):
         n, m = fileIn.readline().split()
         intervals.append([int(n), int(m)])

   out = ''
   for i, interval in enumerate(intervals):
      #print "***"
      out += "Case #{n}: {s}\n".format(n=i+1, s=solve(interval))

   with open('C-small.out', 'w') as fileOut:
      fileOut.write(out)
      print out

if __name__ == "__main__":
   main()
