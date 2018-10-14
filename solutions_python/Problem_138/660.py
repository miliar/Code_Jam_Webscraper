def comp(l1,l2):
    while len(l1)>0:
        a = l1.pop()
        if l2[len(l2)-1] > a:
            m = l2.pop()
    return len(l2)

f = [line.rstrip() for line in open('/Users/roshil/Desktop/D-large.in')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for i in range(1, testcases+1):
    n = int(f[line])
    line += 1
    naomi1 = [float(num) for num in f[line].split()]
    naomi2 = [float(num) for num in f[line].split()]
    line +=1
    ken1 =  [float(num) for num in f[line].split()]
    ken2 =  [float(num) for num in f[line].split()]
    line +=1
    naomi1.sort()
    ken1.sort()
    x = comp(naomi1,ken1)
    naomi2.sort()
    ken2.sort()
    y = n - comp(ken2,naomi2)
    out.write("case #"+str(i)+": "+str(y) + " " +str(x) + "\n")
out.close()
    
    