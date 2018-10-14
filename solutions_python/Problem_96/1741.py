__author__ = 'amoscati'
import copy

f = open('input.txt')
output = open('output.txt', 'w')
lines = [ line for line in f]
T = int(lines[0])

index = 1
while (index < len(lines)):
    t = 0
    while (t < T):
        t = t + 1
        l = lines[index].split()
        N,S,p = int(l[0]),int(l[1]),int(l[2])
        l = [int(i) for i in l[3:3+N]]
        index = index + 1

        l1 = [i for i in l if i >= (p * 3 - 2)]
        print l1
        l2 = []
        if p > 1:
            l2 = [i for i in l if i == (p * 3 - 4) or i == (p * 3 - 3)]
        print l2
        o = len(l1) + min(len(l2), S)



        #print
        print N,S,p,l
        print 'Case #%d: %d' % (t,o)
        output.write('Case #%d: %d\n' % (t,o))




