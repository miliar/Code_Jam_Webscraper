"""
SeeNoEvil's Solution to the problem A, GCJ 2009, Round 1A

Note: non-standard package psyco can be obtained from:
http://psyco.sourceforge.net/
"""

import sys

def ToBase(b, n):
   """
   >>> ToBase(2, 9)
   1001
   >>> ToBase(3, 9)
   100
   """
   d = []
   while n:
      d.append(n % b)
      n //= b
   d.reverse()   
   return int(''.join(map(str, d)))   
   
def Happy(n, b):
   """
   >>> Happy(82, 10)
   True
   >>> Happy(82, 3)
   False
   """
   n = ToBase(b, n)
   seen = set()
   while n not in seen:
      seen.add(n)   
      v = 0
      while n:
         d = n % 10
         n = n // 10
         v += d * d
      n = ToBase(b, v)   
      if n == 1:
         return True
   return False                   
   
def Solve(bases):
    """
    >>> Solve([2,3])
    3
    >>> Solve([2,3,7])
    143
    >>> Solve([9,10])
    91
    """
    n = 1
    while 1:
       n += 1
       done = True
       for b in bases:
          if not Happy(n, b):
             done = False
             break
       if done:
          return n       
     
def main():
    fin = file(sys.argv[1])
    fout = file(sys.argv[2], "wt")

    numCases = int(fin.readline())
    for case in xrange(numCases):
        bases = map(int, fin.readline().split())
        fout.write("Case #%d: %d\n" % (case+1, Solve(bases)))
   
if __name__ == "__main__":

    #try:
    #    import psyco
    #    psyco.bind(Add)
    #except ImportError:
    #    print 'Psyco not installed, the program will just run slower'

#    import cProfile
#    import pstats
#    cProfile.run("main()", "gcj.prof")
#    pstats.Stats("gcj.prof").strip_dirs().sort_stats(-1).print_stats()

    import doctest
    doctest.testmod()
   
    main()   
  