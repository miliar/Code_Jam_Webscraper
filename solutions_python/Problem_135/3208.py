import sys
fin = open('A-small-attempt0.in')
N = int(fin.readline())
for case in range(1,N+1):
    G = int(fin.readline())
    array=[]
    for i in range(4):
        line=fin.readline()
        array.append([int(x) for x in line.split()])
    H=int(fin.readline())
    array2=[]
    for i in range(4):
        line2=fin.readline()
        array2.append([int(x) for x in line2.split()]) 
    s1=array[G-1]
    s2=array2[H-1]
    s3=list(set(s1).intersection(s2))
    if len(s3)==1: 
        print "Case #%d: %d" % (case, s3[0])
    if len(s3) > 1:
        print "Case #%d: Bad magician!" % (case)
    if len(s3) < 1:
        print "Case #%d: Volunteer cheated!" % (case)
    