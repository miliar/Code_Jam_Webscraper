ln = '\n'
filename = 'a.txt'
r = open(filename,'r')
w = open('out.txt','w')
t = int(r.readline())
k = 1
while k<=t:
    n,l,h = map(int,r.readline().strip().split())
    nn = map(int,r.readline().strip().split())
    w.write('Case #%d: ' % k)
    for i in range(l,h+1):
        flag = False
        for j in nn:
            if j>i:
                if j%i!=0:
                    flag = True
                    break
            else:
                if i % j != 0:
                    flag = True
                    break
        if not flag:
            w.write(str(i))
            break
    if flag:
        w.write("NO")
    w.write('\n')
    k+= 1
r.close()
w.close()
