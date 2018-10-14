with open('B-small-attempt1.in', 'r') as fin:
    with open('Bout.txt', 'w') as fout:
        n = int(fin.readline())
        for i in range(n):
            line = [int(x) for x in fin.readline().split()]
            #print line[0], line[1], line[2]
            vals = [a & b for a in range(line[0]) for b in range(line[1]) if a & b < line[2]]
            #print len(vals)
            fout.write('Case #'+str(i+1)+': '+str(len(vals))+'\n')
