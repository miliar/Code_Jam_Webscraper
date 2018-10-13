import sys

in_name = 'C-small-attempt0.in'
in_name = 'C-large.in'
out_name = 'c_out.txt'
fin = open(in_name, 'r')
fout = open(out_name, 'w')

n = fin.readline()
n = int(n.split('\n')[0])
res = []

for i, line in enumerate(fin):
    value = 0
    line = line.split()
    A, B = int(line[0]), int(line[1])
    recycled = {}
    for n in range(A, B+1):        
        if n < 10 or n in recycled:
            continue
        
        # Create list of hoan vi of n
        hv = []
        hv.append(n)
        mag = len(str(n))
        for j in range(1, mag):
            tail = n/10**j
            head = n % 10**j
            m = head*(10**(mag-j)) + tail
            if A <= m <= B and m >= 10**(mag - 1) and m != n and not m in hv:
                hv.append(m)
                recycled[m] = True
        
        recycled[n] = True
        count = 0
        for k in range(len(hv) - 1):
            for h in range(k+1, len(hv)):                
                count += 1
        value += count
        # if count > 0:
            # print 'hv',hv, count
    #print recycled    
    res.append("Case #%d: %s\n" % (i+1, value))
    
fout.writelines(res)
fout.close()
fin.close()