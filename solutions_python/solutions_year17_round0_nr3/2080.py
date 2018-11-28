f = open('C-small-1-attempt0.in', 'r')
g = open('C-small-1-attempt0.out', 'w')
t_c = int(f.readline().strip())
c = 1

while(c <= t_c):
    line = f.readline().strip().split()
    n = int(line[0])
    k = int(line[1])
    x = '0' + n*'.' + '0'
    x_ = list(x)
    #print line
    while(k):
        
        first = x.find('.')
        old_ls = first - (x.rfind('0', 0, first)+1)
        old_rs = (x.find('0', first)-1) - first
        mi = min([old_ls, old_rs])
        ma = max([old_ls, old_rs])
        #print old_ls, old_rs, mi, ma
        p = first
        for i in range(first+1, len(x)-1):
            if x[i] == '.':
                ls = i - (x.rfind('0', 0, i)+1)
                rs = (x.find('0', i)-1) - i
                
                #print ls, rs, min([ls, rs]), max([ls, rs])
                if min([ls, rs]) > mi:
                    mi = min([ls, rs])
                    ma = max([ls, rs])
                    p = i
                    old_ls = ls
                    old_rs = rs
                elif min([ls, rs]) == mi and max([ls, rs]) > ma:
                    mi = min([ls, rs])
                    ma = max([ls, rs])
                    p = i
                    old_ls = ls
                    old_rs = rs                
                    
        x_[p] = '0'
        x = ''.join(x_)
        #print x
        if k == 1:
            g.write("Case #"+str(c)+': '+str(max([old_ls, old_rs]))+' '+str(min([old_ls, old_rs]))+'\n')
            print "Case #"+str(c)+': '+str(max([old_ls, old_rs]))+' '+str(min([old_ls, old_rs]))+'\n'
            #print p, old_ls, old_rs
        k -= 1
    c += 1
g.close()  