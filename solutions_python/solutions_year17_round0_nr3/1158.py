import math
data = open('C-small-2-attempt0.in','r')
d = open('C-small-2-attempt0.out','w')

cases = int(data.readline())
for x in range(cases):
    stalls,people = map(int,data.readline().split())

    pos = (math.ceil(math.log(people+1)/math.log(2)))-1
    limit = (stalls%(2**pos)) + 1
    mx_mn = int(stalls/(2**pos))
    if people < ((2**(pos))+limit):mx_mn = mx_mn
    else: mx_mn -=1
    mx = int(mx_mn/2);mn = mx_mn - mx - 1
    #print ('Case #' + str(x+1) + ': ' + str(mx) + ' ' + str(mn))
    print >>d,('Case #' + str(x+1) + ': ' + str(mx) + ' ' + str(mn))
    
d.close()
