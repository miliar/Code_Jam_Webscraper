"""
SeeNoEvil's Solution to the "Minimum Scalar Product" problem, GCJ 2008, Round 1

Note: non-standard package psyco can be obtained from:
http://psyco.sourceforge.net/
"""

import sys

def MSP(v1, v2):
    """
    Set the global variable to the specified value.
    >>> MSP([1,2,3],[1,2,3])
    10
    """
    v1.sort()
    v2.sort(reverse=True)
    sp = 0
    for n in xrange(len(v1)):
      sp += v1[n] * v2[n]
    return sp
     
def main():
    fin = file(sys.argv[1])
    fout = file(sys.argv[2], "wt")

    numCases = int(fin.readline())
    for case in xrange(numCases):
        size = int(fin.readline())
        v1 = map(int, fin.readline().split())
        v2 = map(int, fin.readline().split())
        assert size == len(v1) and size == len(v2)
        fout.write("Case #%d: %d\n" % (case+1, MSP(v1, v2)))
   
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
  