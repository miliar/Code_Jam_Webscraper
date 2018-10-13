#Read input file with extension .in
#for path in files:
#    if path.find('.in') != -1:
#        break
#print path
path ='A-small-attempt0.in'
f = open(path)
o = open('output.out','w')
cases=int(f.readline())

for case in xrange(1,cases+1):
    row1 = int(f.readline())
    for i in xrange(1,5):
        if i == row1:
            row1 = [int(z) for z in f.readline().strip().split(' ')]
        else:
            f.readline()
    row2 = int(f.readline())
    for i in xrange(1,5):
        if i == row2:
            row2 = [int(z) for z in f.readline().strip().split(' ')]
        else:
            f.readline()
    result = filter(lambda x: x in row1,row2)
    if len(result)==1:
        o.write('Case #%d: %d\n' % (case,result[0]))
    elif len(result)>1:
        o.write('Case #%d: Bad magician!\n' % (case))
    else:
        o.write('Case #%d: Volunteer cheated!\n' % (case))


f.close()
o.close()
