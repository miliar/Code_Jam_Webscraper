# coding: utf-8

"""
Problem

"""
foutput  = open('A-large.out', 'w')

i = 0
for line in open('A-large.in', 'r'):
        item = line[:-1].split()
        if len(item) == 1:continue
        light = 'OFF'
        i += 1
        n = int(item[0])
        k = int(item[1])
#        print item
        if (k != 0) and ((k + 1) % (2**n) == 0):
                light = 'ON'
        result = "Case #" + str(i) + ": " + light + '\n'
#        print result,
        foutput.write(result)
foutput.close()
