import sys, math
cases = int(sys.stdin.readline())
for count in range(cases):
    arr=[]
    k_n = sys.stdin.readline().split(' ')
    k,n= int(k_n[0]), int(k_n[1])
    power= int(math.pow(2,math.ceil(math.log(n+1,2))))
    max_d = (k-n+(power/2)) / power
    min_d = (k-n) / power
    print "Case #%s: %s %s"%(count+1,max_d,min_d)
