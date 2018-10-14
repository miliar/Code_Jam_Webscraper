import sys
def check_tidy(n):
    num = str (n)
    if len(num) == 1 :
        return 1
    else :
        if all(num[i] <= num[i+1] for i in xrange (0, len(num)-1)) :
            return 1
        else :
            return 0

    
with open(sys.argv[1],'r') as files : 
    t = int (files.readline())
    result = [ 0, 0]
    for i in xrange(1, t + 1):
        n = int (files.readline())
        for j in xrange (1, n+1 ):
            check = check_tidy(j)
            pos = int(bool(1) & bool(check))
            result[pos] = check * j
        print "Case #{}: {}".format(i,result[-1])
        result = [0, 0]


