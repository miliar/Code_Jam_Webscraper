ln = '\n'
filename = 'a.txt'
r = open(filename,'r')
w = open('out.txt','w')
t = int(r.readline())
k = 1
while k<=t:
    n = int(r.readline().strip())
    x1 = []
    x2 = []
    x3 = []
    yy = []
    for i in range(n):
        yy.append(r.readline().strip())
    
    for i in yy:
        suc = 0
        los = 0
        for j in i:
            if j == '1':
                suc += 1
            elif j=='0':
                los += 1
        x1.append(float(suc)/(suc+los))

    for i in range(n):
        acc = 0
        sun = 0
        for j in range(n):
            if j == i:
                continue
            if yy[i][j]=='0' or yy[i][j]=='1':
                suc = 0
                los = 0
                for kk in range(n):
                    if kk==i:
                        continue
                    if yy[j][kk]=='1':
                        suc += 1
                    elif yy[j][kk]=='0':
                        los += 1
                sun += (float(suc)/(suc+los))
                acc += 1
        x2.append(sun/acc)

    for i in range(n):
        acc = 0
        sun = 0
        for j in range(n):
            if j==i:
                continue
            if yy[i][j]=='0' or yy[i][j]=='1':
                sun += x2[j]
                acc += 1
        x3.append(float(sun)/acc)


    w.write('Case #%d:\n' % k)
    for i in range(n):
        w.write("%s\n" %  str(0.25*x1[i]+0.5*x2[i]+0.25*x3[i]))
    k += 1

r.close()
w.close()
"""
    for i in range(n):
        acc = 0
        sun = 0
        for j in range(n):
            suc = 0
            los = 0
            if j == i:
                continue
            if yy[i][j]=='0' or yy[i][j]=='1':
                for k in range(n):
                    if k==i:
                        continue
                    if yy[j][k]=='1':
                        suc += 1
                    elif yy[j][k]=='0':
                        los += 1
            sun += (float(suc)/(suc+los))
            acc += 1
            x2.append(sun/acc)
"""
