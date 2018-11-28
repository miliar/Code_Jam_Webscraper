#

#import sys, StringIO

#infile = StringIO.StringIO('''4
#1 0
#1 1
#4 0
#4 47
#''')

#infile = sys.stdin
infile = open('A-large.in', 'r')
outfile = open('A-large.out', 'w')

NTrials = int(infile.readline())

for t in range(NTrials):
    n, k = map(int, infile.readline().split())
    lightOn = (k + 1) % (1 << n) == 0
    outfile.write('Case #{0}: {1}\n'.format(t + 1, lightOn and 'ON' or 'OFF'))

infile.close()
outfile.close()
