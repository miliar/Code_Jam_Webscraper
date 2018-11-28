f = open('C-large.in', 'r')
fout = open('c_big.out', 'w')
n = (int)(f.readline())
for i in xrange(n):
    print i
    sp = f.readline().split(' ')
    a = int(sp[0])
    b = int(sp[1])
    count = 0
    for num in range(a, b+1):
        numStr = str(num)
        mark = []
        for k in range(1,len(numStr)):
            newNum = int(numStr[k:] + numStr[:k])
            if newNum>=a and newNum<=b and newNum>num and len(str(newNum))==len(numStr) and not (newNum in mark):
                count += 1
            mark.append(newNum)
    fout.write("Case #" + str(i+1) + ": " + str(count) + "\n")
fout.close()
