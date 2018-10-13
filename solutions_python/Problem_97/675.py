from sys import stdin

def recycled_num(a,b):
    frmt = '%0'+str(len(str(a)))+'d'
    recycled = 0

    for n in xrange(a,b+1):
        sn = frmt%n
        lset = set()
        for i in range(1,len(sn)):
            m = int(sn[-i:] + sn[:-i])
            if m >= a and m > n and m <= b:
                lset.add(m)                
        recycled += len(lset)

##        if len(lset) > 0:
##            print '%d %s'%(n,lset)
            
    return recycled

num_cases = int(stdin.readline())
for case_index in xrange(1, num_cases+1):
    a,b = map(int,stdin.readline().strip().split(' '))            
    print "Case #" + str(case_index) + ": " + str(recycled_num(a,b))
