from __future__ import print_function
import os, os.path
directory = 'C:\Users\lucho\Desktop\___tests'
files = os.listdir(directory)
fp = open(os.path.join(directory, files[0]), 'rb')

fp2 = open(os.path.join(directory, '..', 'out2.out'), 'wb')

lines = fp.readlines()
tests = int(lines[0].strip())
for i in range(tests):
    data = map(int, lines[2+2*i].split())
    if reduce(lambda a,b: a^b, data) == 0:
        print('Case #%d: %d' % (i+1, sum(data) - min(data)), file=fp2)
    else:
        print('Case #%d: NO' % (i+1), file=fp2)

fp.close()
fp2.close()
