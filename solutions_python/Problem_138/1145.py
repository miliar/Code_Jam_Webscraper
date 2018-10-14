#!/usr/bin/python
import sys, getopt

__author__ = 'cdriscoll'


class War: 
    caseNum = 0
    N = 0
    naomi = []
    ken = []

    def __init__(self, caseNum, N, naomi, ken):
        self.caseNum = caseNum
        self.N = N
        self.naomi = naomi
        self.ken = ken

    def rotate(self, array):
      temp = array[self.N - 1]
      array = array[:self.N-1]
      array.insert(0, temp)
      return array

    def solve(self):
      war = 0
      dwar = 0
      snaomi = sorted(self.naomi, reverse=True)
      sken = sorted(self.ken, reverse=True)
      for i in range(0, self.N):
        if (snaomi[i] > sken[i]):
          war += 1
          sken = self.rotate(sken)
      sken = sorted(self.ken, reverse=True)
      for i in range(0, self.N):
        if (sken[i] > snaomi[i]):
          snaomi = self.rotate(snaomi)
        else:
          dwar += 1

      return "Case #%d: %d %d\n" % (self.caseNum, dwar, war)


def main(argv):
    infile = ''
    outfile = ''


    try:
        opts, args = getopt.getopt(argv, "i:o:", ["ifile=", "ofile"])
    except getopt.GetoptError:
        #print 'magic.py -i <inputfile> -o <outputfile'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            infile = arg
        elif opt in ("-o", "--ofile"):
            outfile = arg

    fd_in = open(infile, 'r')
    fd_out = open(outfile, 'a')

    numTests = int(fd_in.readline())

    for i in range(1, numTests + 1):
        N = int(fd_in.readline())
        naomi = map(float, fd_in.readline().split(' '))
        ken   = map(float, fd_in.readline().split(' '))
        #print "%f, %f, %f\n" % (C, F, X)
        test = War(i, N, naomi, ken)
        fd_out.write(test.solve())




if __name__ == '__main__':
    main(sys.argv[1:])
