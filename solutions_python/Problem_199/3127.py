def pan(l,k):
    l = [w for w in l]
    count = 0
    for i in range(len(l)-k+1):
        if l[i] == '-':
            for j in range(i, i+k):
                if l[j] == '-':
                    l[j] = '+'
                else:
                    l[j] = '-'
            count += 1
            #print l
    if '-' in l:
        count = 'IMPOSSIBLE'
    return count

f = [line.rstrip() for line in open('/Users/roshil/Desktop/A-small-attempt0 (2).in')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for j in range(1, testcases+1):
    m = f[line].split()
    line += 1
    l,k = m[0], int(m[1])
    ans = pan(l,k)
    out.write("Case #"+str(j)+": "+str(ans) + "\n")
    #print "case #"+str(j)+": "+str(ans) + "\n"
out.close()