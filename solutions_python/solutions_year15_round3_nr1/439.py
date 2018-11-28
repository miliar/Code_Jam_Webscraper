#from __future__ import division
#import math
fin = open("C:/Users/rajiv/Desktop/code jam 15/A-small-attempt0.in", "r")
f = open('C:/Users/rajiv/Desktop/code jam 15/A-small-attempt0.out', 'w')

cases = int(fin.readline())

for i in range(cases):
    #d = fin.readline()
    d=[int(x) for x in fin.readline().split()]
    result=d[1]/d[2]+(d[2]-1)
   # print(d)

    print ("Case #%d: %d" % (i + 1, result))
    f.write("Case #%d: %d" % (i + 1, result) + '\n')
f.close()

