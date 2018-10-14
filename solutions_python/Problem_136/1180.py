#!/usr/bin/python
import sys, getopt

__author__ = 'cdriscoll'


class Cookie: 
    caseNum = 0
    C = 0.0
    F = 0.0
    X = 0.0

    def __init__(self, caseNum, C, F, X):
        self.caseNum = caseNum
        self.C = C
        self.F = F
        self.X = X

    def solve(self):

        origRate  = 2.0
        timeNoF   = self.X / origRate
        r1  = origRate + self.F
        Xr1 = self.X / r1
        Cr1 = self.C / origRate
        r2  = r1 + self.F
        Xr2 = self.X / r2
        Cr2 = self.C / r1
        timeToFprev = Cr1

        time1 = Xr1 + Cr1
        #print "Time 1 [%.7f] [%f, %f, %f]" % (time1, r1, Xr1, Cr1)
        if (time1 > timeNoF):
          return "Case #%d: %.7f\n" % (self.caseNum, timeNoF)
 
        time2 = Xr2 + Cr2 + timeToFprev
        #print "Time 2  [%.7f] [%f, %f, %f, %f]" % (time2, r2, Xr2, Cr2, timeToFprev)

        while (time2 < time1):
          timeToFprev += Cr2
          time1 = time2
          r1 = r2
          #print "Time 1 [%.7f]" % time1
          r2  = r1 + self.F
          Xr2 = self.X / r2
          Cr2 = self.C / r1
          time2 = Xr2 + Cr2 + timeToFprev
          #print "Time 2  [%.7f] [%f, %f, %f, %f]" % (time2, r2, Xr2, Cr2, timeToFprev)
        
        #print "\n"
        return "Case #%d: %.7f\n" % (self.caseNum, time1)

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
        test = map(float, fd_in.readline().split(' '))
        C = test[0]
        F = test[1]
        X = test[2]
        #print "%f, %f, %f\n" % (C, F, X)
        test = Cookie(i, C,F,X)
        fd_out.write(test.solve())




if __name__ == '__main__':
    main(sys.argv[1:])
