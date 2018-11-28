__author__ = 'jesus'

FILE = 'qual-a.in'
FILEOUT = 'qual-a.out'

f = open(FILE, 'r')
fout = open (FILEOUT, 'w')

testcases = int(f.next())
for icase in range (1, testcases+1):

    answer1 = int(f.next())-1
    for i in range(4):
        if (i==answer1):
            row1 = f.next().split()
        else:
            f.next()

    answer2 = int(f.next())-1
    for i in range(4):
        if (i==answer2):
            row2 = f.next().split()
        else:
            f.next()

    print row1
    print row2

    set1 = set(row1)
    set2 = set(row2)
    print set1
    print set2
    s = {}
    s = set1.intersection(set2)
    print s

    l = len (s)
    if l==0:
        fout.write ("Case #{0}: {1}\n".format (icase, 'Volunteer cheated!'))
    elif l==1:
        fout.write ("Case #{0}: {1}\n".format (icase, s.pop()))
    else:
        fout.write ("Case #{0}: {1}\n".format (icase, 'Bad magician!'))

f.close()
fout.close()
