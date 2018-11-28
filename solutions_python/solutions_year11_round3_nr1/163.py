ln = '\n'
filename = 'a.txt'
r = open(filename,'r')
w = open('out.txt','w')
t = int(r.readline())
k = 1
while k<=t:
    a,b = map(int,r.readline().strip().split())
    ss = []
    for i in range(a):
        ss.append(list(r.readline()))
    for i in range(a-1):
        for j in range(b-1):
            if ss[i][j]=='#' and ss[i][j+1]=='#' and ss[i+1][j]=='#' and ss[i+1][j+1] == '#':
                ss[i][j] = '/'
                ss[i][j+1]= '\\'
                ss[i+1][j] = '\\'
                ss[i+1][j+1] = '/'

    flag = True
    for i in range(a):
        for j in range(b):
            if ss[i][j]=='#':
                flag = False
                break
        if not flag:
            break
    w.write('Case #%d:\n' % k)
    k += 1
    if not flag:
        w.write("Impossible\n")
    else:
        for i in range(a):
            for j in range(b):
                w.write(ss[i][j])
            w.write('\n')

r.close()
w.close()
