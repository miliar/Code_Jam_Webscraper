"""Code Jam - Speaking in Tongues

Solution to Google Code Jam 2012 Qualification Round Problem A
"""

import sys
import string

cipher = string.maketrans('ynficwlbkuomxsevzpdrjgthaq', 'abcdefghijklmnopqrstuvwxyz')


def main(argv=None):

    # Setup arguments
    if argv is None:
        argv = sys.argv

    # Setup IO
    fin = open(argv[1], 'r')
    fout = open(argv[0] + '.out', 'w')

    # Read in data
    casesCount = fin.readline()
    cases = fin.readlines()

    # Process each case
    i = 1
    for case in cases:
        fout.write("Case #%d: %s" % (i, string.translate(case, cipher)))
        print "Case #%d: %s" % (i, string.translate(case, cipher))
        i += 1

    fin.close()
    fout.close()

if __name__ == "__main__":
    sys.exit(main())
