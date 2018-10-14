f = [line.rstrip() for line in open('/Users/roshil/Desktop/B-large.in')]
out = open('/Users/roshil/Desktop/output','w')
out.truncate()
line = 0
testcases = int(f[line])
line += 1
for i in range(1, testcases+1):
    dat  = [float(num) for num in f[line].split()]
    line += 1
    C,F,X = dat[0],dat[1],dat[2]
    nf = 0
    if X<C:
        time = X/2.
    else:
        time = 0
        while C/(2+F*nf)+ X/(2+F*(nf+1)) < X/(2+F*nf):
               time += float(C/(2+F*nf))
               nf= nf+1
        time +=float((X/(2+F*nf)))
    out.write("case #"+str(i)+": "+str(time) + "\n")
    #print "case #"+str(i)+": "+str(time) + "\n"
out.close()
        