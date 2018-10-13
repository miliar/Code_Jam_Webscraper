with open("in.txt", "r") as f:
    with open("out.txt", "w") as fo:
        n = int(f.readline())
        for i in range(n):
            r = int(f.readline())
            r1 = []
            r2 = []
            for j in range(4):
                if(j == r-1):
                    r1 = f.readline().rstrip().split(' ')
                else:
                    f.readline()
            r = int(f.readline())
            for j in range(4):
                if(j == r-1):
                    r2 = f.readline().rstrip().split(' ')
                else:
                    f.readline()
            s = set(r1) & set(r2)
            if(len(s) < 1):
                fo.write('Case #%(case)d: Volunteer cheated!\n' % {'case': i+1})
            elif len(s) > 1:
                fo.write('Case #%(case)d: Bad magician!\n' % {'case': i+1})
            else:
                fo.write('Case #%(case)d: %(res)s\n' % {'case': i+1, 'res':list(s)[0]})