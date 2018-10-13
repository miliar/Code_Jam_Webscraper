from decimal import *
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", metavar="FILE")
(options, args) = parser.parse_args()

if options.filename is None:
        parser.print_help()
        exit()
try:
        FILE = open(options.filename)
except IOError:
        print "File", options.filename, "does not exist"
        exit()
        
# Number of test cases
N = int(FILE.readline().rstrip())
for i in xrange(N):
        # P = Maximum number of letters to place on a key
        # K = Number of keys available
        # L = number of letters in our alphabet
        (P, K, L) = [int(x) for x in FILE.readline().rstrip().split(" ")]
        freqs = sorted([int(x) for x in FILE.readline().rstrip().split(" ")])
        freqs.reverse()
        counter = 0
        res = 0
        while freqs:
                counter += 1
                res += sum(freqs[:K])*counter
                del freqs[0:K]
        print "Case #" + str(i+1) + ": " + str(res)
                
