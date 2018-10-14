infile = open('d:\Desktop\A-large.in').readlines()
outfile = open('A-large.out', 'w')
for i, s in enumerate(infile[1:]):
    a = b = 0
    s = s.split(' ')[1].strip()
    for d in s:
        a += int(d)
        if a == 0:
            b += 1
        else:
            a -= 1
    outfile.write('Case #' + str(i+1) + ': ' + str(b) + '\n')
outfile.close()
