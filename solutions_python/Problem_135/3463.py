with open('A-small.in') as in_put:
    content = in_put.readlines()

content = [line.strip('\n') for line in content]

N = int(content[0])

with open('A-small.out', 'w') as out_put:
    for case in xrange(min(N,100)):
        row1 = int(content[10*case+1])
        row2 = int(content[10*case+6])
        if row1 not in range(1,5) or row2 not in range(1,5):
            print ("Error! Rows out of bounds")
        line1 = content[10*case+1+row1].split()
        line1 = set([int(i) for i in line1])
        line2 = content[10*case+6+row2].split()
        line2 = set([int(i) for i in line2])
        cards = line1 & line2
        if not cards:
            out_put.write("Case #%d: Volunteer cheated!\n" % (case+1,))
        elif len(cards) > 1:
            out_put.write("Case #%d: Bad magician!\n" % (case+1,))
        else:
            out_put.write("Case #%d: %s\n" % (case+1,cards.pop()))
        #out_put.write("Case #%d: %s\n" % (case+1,enil))

