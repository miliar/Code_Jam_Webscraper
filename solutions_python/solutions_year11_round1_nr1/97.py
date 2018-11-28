#!/usr/bin/python
from sys import argv


def calculate_statistics(N, today, ever):
    if ever == 100 and today < 100:
        return 'Broken'
    if ever == 0 and today > 0:
        return 'Broken'
    if today % 100 == 0:
        X=1
    elif today % 50 == 0:
        X=2
    elif today % 25 == 0:
        X=4
    elif today % 20 == 0:
        X=5
    elif today % 10 == 0:
        X=10
    elif today % 5 == 0:
        X=20
    elif today % 4 == 0:
        X=25
    elif today % 2 ==0:
        X=50
    else:
        X=100
    if N < X:
        return 'Broken'
    else:
        return 'Possible'


def freecell(input_file, output_file):
    f=open(input_file, 'r')
    N=int(f.readline())
    g=open(output_file, 'w')
    for i in xrange(N):
        line=f.readline()
        x=line.split(' ')
        stat=calculate_statistics(int(x[0]), int(x[1]), int(x[2]))
        g.write('Case #'+str(i+1)+': ')
        g.write(stat+'\n')
    f.close()
    g.close()


#run: python candy.py input output
if __name__=='__main__':
    if argv[0].find('freecell.py')!=-1:
        if len(argv)>=3:
            freecell(argv[1], argv[2])
