ip = open('B-large.in')
op = open('out.out', 'w')
n = int(ip.readline())
for a in xrange(n):
    t = map(int, str(ip.readline()).split())
    n = t.pop(0)
    s = t.pop(0)
    p = t.pop(0)
    count = 0
    if p==0:
        op.write('Case #'+str(a+1)+': '+str(n)+'\n')
        continue
    elif p==1:
        op.write('Case #'+str(a+1)+': '+str(n-t.count(0))+'\n')
        continue
    for i in t:
        if i>=(3*p-2):
            count += 1
        elif i>=(3*p-4) and s!=0:
            count += 1
            s -= 1
        else:
            pass
    op.write('Case #'+str(a+1)+': '+str(count)+'\n')
ip.close()
op.close()
