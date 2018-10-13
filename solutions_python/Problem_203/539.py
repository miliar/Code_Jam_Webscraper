def cake(l):
    for i,a in enumerate(l):
        if len(set(a))==1 and a[0] == '?' and i!= 0:
            if l[i-1][0]!='?':
                l[i] = l[i-1]
        else:
            for b in range(len(a)):
                if a[b] != '?':
                    for u in range(max(0,b-1),-1,-1):
                        if a[u] == '?':
                            a[u] = a[b]
                        else:
                            break
                    for v in range(min(len(a)-1,b+1),len(a)):
                        if a[v] == '?':
                            a[v] = a[b]
                        else:
                            break
    l.reverse()
    for i,a in enumerate(l):
        if len(set(a))==1 and a[0] == '?':
            if i!= 0:
                if l[i-1][0]!='?':
                    l[i] = l[i-1]
    l.reverse()
    return l
f = [line.rstrip() for line in open('/Users/roshil/Desktop/A-small-attempt2.in')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for j in range(1, testcases+1):
    m = f[line].split()
    line += 1
    n1,n2 = m[0], int(m[1])
    ll = []
    for z in range(int(n1)):
        temp = [a for a in f[line]]
        ll.append(temp)
        line  += 1
    ans = cake(ll)
    out.write("Case #"+str(j)+":"+ "\n")
    #print "Case #"+str(j)+":"+ "\n"
    for lll in ans:
        out.write(''.join(lll) + "\n")
        #print ''.join(lll)
    print "case #"+str(j)+": "+str(ans) + "\n"
out.close()