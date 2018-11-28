import sys

from Round1ProblemB import r1pb

if __name__ == '__main__':
    args = sys.argv
    if (len(args) < 2):
        print "Not enough args"
        print "Usage: testFileToRead"
        exit()
    fileName = sys.argv[1]
    fh = open(fileName, 'r')
    r1pb.main(fh.read())
    exit(0)


