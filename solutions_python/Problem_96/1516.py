def handleCase(line):
    a = line.split(' ')
    S = int(a[1])
    p = int(a[2])
    good = max(0,(p*3)-2)
    sup = max(0,(p*3)-4)
    res = 0
    for i in range(3,len(a)):
        sc = int(a[i])
        if (sc == 0):
                if(p==0):
                    res += 1
                continue
        if (sc >= good):
            res += 1
        elif (sc >= sup and S > 0) :
            res += 1
            S -= 1

    return str(res) + '\n'

inf = file('C:\\temp\\in.txt', 'r')
outf = file('C:\\temp\\out.txt', 'w')
c = int(inf.readline().replace('\n',''))
for i in range(c):
    outf.write("Case #" + str(i+1) + ": " + handleCase(inf.readline().replace('\n','')))

inf.close()
outf.close()
    
