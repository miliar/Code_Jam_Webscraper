fin = open('B-small-attempt0.in')
N = int(fin.readline())
for case in range(1,N+1):
    array=[]
    line=fin.readline()
    array.append([int(x) for x in line.split()]) 
    m=array[0]
    count=0
    for i in range(m[0]):
        for j in range(m[1]):
            an=i&j
            if (an<m[2]):
                count=count+1        
    print "Case #%d: %d" % (case, count)
    