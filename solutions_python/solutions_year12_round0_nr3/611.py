def recNum(a, b):
    x, y, count = str(a), str(b), 0
    l, n = len(y), a
    while n <= b:
        ns = str(n)
        for i in xrange(len(ns)):
            m = int(ns[-i-1:]+ns[:-i-1])
            if (n<m and m<=b):
                equal = 0 
                for j in xrange(i):
                    k = int(ns[-j-1:]+ns[:-j-1])
                    if m==k:
                        equal = 1
                        break
                if not equal:
                    count += 1
        n += 1
    return count
        
infile = open('a')
outfile = open('b', 'w')   
infile.readline()
counter = 1
for line in infile:
    outfile.write('Case #'+str(counter)+': ')
    l = line.split()
    outfile.write(str(recNum(int(l[0]), int(l[1]))))
    outfile.write('\n')
    counter += 1


     
