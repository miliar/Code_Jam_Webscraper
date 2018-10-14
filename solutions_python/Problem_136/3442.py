fin = open('B.in','r')
fout = open('B.out','w')

case = int(fin.readline())

for i in range(case):

    line = fin.readline()
    ddd = line.rstrip()
    lll = ddd.split(' ')
    c = float(lll[0])
    f = float(lll[1])
    x = float(lll[2])
    ps = 2.0
    dt = c/f

    tt = (x-c) / ps
    cc = 0
    time = 0

    if c > x:
        time = round(x/ps,7)
        fout.write('Case #{}: {}'.format(str(i+1),"{0:.7f}".format(time).rstrip()))
        fout.write('\n')

    else:
        while(tt > dt):
            time += round(c/ps,7)
            cc += 1
            ps += f
            tt = (x-c) / ps
            tt = round(tt,7)

        time += x/ps
        time = round(time,7)
        fout.write('Case #{}: {}'.format(str(i+1),"{0:.7f}".format(time)).rstrip())
        fout.write('\n')


fin.close()
fout.close()