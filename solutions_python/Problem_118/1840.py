from math import *
from sys import *
def is_palindrome(w):
    return w == '' or w[0] == w[-1] and is_palindrome(w[1:-1])
nb=0


f = open('input')
nb =int(f.readline().split()[0])
for case in range(1,(nb + 1)):
  nb = 0
  w, h = [int(x) for x in f.readline().split()]
  for i in range(w,h+1):
    if is_palindrome(str(i)):
     sqrti = sqrt(i)
     if sqrti.is_integer():
       if is_palindrome(str(int(sqrti))):
         nb = nb + 1
  print "Case #%d: %d" % (case,nb)

f.close();
