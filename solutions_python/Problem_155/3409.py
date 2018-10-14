f = [line.rstrip() for line in open('/Users/roshil/Desktop/A-large.in')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for j in range(1, testcases+1):
    dat  = [num for num in f[line].split()]
    line += 1
    smax, temp = int(dat[0]),dat[1]
    ans = 0
    si = [int(i) for i in str(temp)]
    #print si
    yoyo = [sum(si[:i+1]) for i in range(smax+1)]
    for i in range(1,smax+1):
        if i > sum(si[:i]):
            ans += i - sum(si[:i])
            si[0] += i - sum(si[:i])
    #print ans
    out.write("case #"+str(j)+": "+str(ans) + "\n")
#print "case #"+str(i)+": "+str(time) + "\n"
out.close()
