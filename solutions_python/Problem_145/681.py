dat = open('A-small-attempt1.in', 'r')
out = open('out.txt', 'w')
t = int(dat.readline())
n=0
flag=0
for i in range(0,t):
    a = str((dat.readline()))
    num, den = a.split('/')
    x = float(num) / float(den)
    for n in range(1,15):
        if int(den)==2**n:
            flag=1
    if flag==0:
        out.write('Case #%d: impossible\n' % (i+1))
        continue
    for j in range(1,41):
        if x >= 0.5:
            out.write('Case #%d: %d\n' % (i+1,j))
            break
        else:
            x*=2
    flag=0

dat.close()
out.close()
                      
