'''
Created on 07/05/2010

@author: jpsantos
'''
from string import rindex

filename = raw_input('Input file:')
infile = open(filename, 'r')
outfile = open("%s.%s"%(filename,'out'), 'w')

tests = int(infile.readline())

for i in range(tests):
    line = infile.readline()
    splitValues = line.split()
    day_times = int(splitValues[0])
    hold = int(splitValues[1])
    groups = int(splitValues[2])
    line = infile.readline()
    clients = line.split()
    next = 0
    riding = 0
    bank = 0
    for ii in range(day_times):
        first = next
        while(riding<=hold):
            riding = riding + int(clients[next])
            next = (next + 1) % groups
            if next == first:
                break;
        if riding > hold:
            riding = riding - int(clients[next-1])
            next = next - 1
        bank = bank + riding
        riding = 0
    print 'Case #%d: %d' % (i+1,bank)
    outfile.write('Case #%d: %d\n' % (i+1,bank))
        