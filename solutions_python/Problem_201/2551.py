import glob
import os.path as path
from shutil import copyfile


def writeline(case, answer):
    outF.write('Case #' + str(case + 1) + ': ' + answer + '\n')


g = glob.glob('C:\\A\\tmp\\*.in')
d = dict()
for item in g:
    d[item] = path.getmtime(item)
inF = open(sorted(d, key=d.__getitem__)[-1], 'r')
outF = open(sorted(d, key=d.__getitem__)[-1].replace('.in', '.out'), 'w')
copyfile('test.py', 'C:\\A\\tmp\\solve.py')

n = int(inF.readline())

for case in range(n):
    answer = ''

    writeline()

