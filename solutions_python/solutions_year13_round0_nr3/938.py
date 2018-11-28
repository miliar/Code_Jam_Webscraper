from sys import stdin

squares = []

def palin(i):
   s = str(i)
   return s == s[::-1]

def gen():
   for i in range(10**7+1):
      if palin(i) and palin(i**2):
         squares.append(i**2)
         #print i**2

def solve( a, b ):
   count = 0
   for i in squares:
      if a <= i and i <= b: count += 1
   return count

gen()
T = int( stdin.readline() )
for i in range(T):
   a, b = (int(j) for j in stdin.readline().strip().split())
   print "Case #{}: {}".format( i+1, solve( a, b ) )
