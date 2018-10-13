def read_row(row, f):
    print 'row', row
    rows_left = 4-row
    while row>0:
        f.readline()
        row -=1
    chosen = f.readline().replace('\n','').split(' ')
    print 'chosen', chosen
    while rows_left>1:
        print 'left', f.readline()
        rows_left -= 1
    return chosen

def magic_trick(filename):
    f = open(filename)
    out = open('magic_trick.out', 'w')
    cases = int(f.readline())
    c = 1
    while c <= cases:
        print "Case #%d" % (c)
        row1 = read_row(int(f.readline())-1, f)
        row2 = read_row(int(f.readline())-1, f)
        
        find = set(row1) & set(row2)
        if len(find) == 1:
            out.write('Case #%d: %s\n' % (c, find.pop()))
        elif len(find) > 1:
            out.write('Case #%d: Bad magician!\n' % (c))
        elif len(find) == 0:
            out.write('Case #%d: Volunteer cheated!\n' % (c))
        c+=1
    f.close()
    out.close()


magic_trick('A-small-attempt0.in')