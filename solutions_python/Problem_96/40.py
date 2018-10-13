fin = open('B-large.in','r')
fout = open('output.out','w')
T = eval(fin.readline())
for i in range(T):
    tmp = fin.readline()
    data = tmp.split()
    n = eval(data[0])
    s = eval(data[1])
    p = eval(data[2])
    point = []
    total = 0
    if p == 1:
        for j in range(n):
            tmp = eval(data[3+j])            
            if tmp > 0:
                total += 1             
    else:
        for j in range(n):
            tmp = eval(data[3+j])            
            if tmp >= 3*p - 2:
                total += 1
            elif tmp >= 3*p - 4 and s > 0:
                total += 1
                s -= 1
	
    print >> fout,"Case #%d: %d" %(i+1,total)
fin.close()
fout.close()
