#T_i = T_{i-1} + (C-X)/(2 + (i-1)*F) + X/(2 + i*F)

f = open('B-large.in', 'r')

T = int(f.readline().strip())

for t in xrange(T):

    (C, F, X) = map(float, f.readline().strip().split(' '))

    T_0 = X/2
    T_i = T_0
    i=1

    while 1:
    
        T_i_1 = T_i
        T_i = T_i_1 + (C-X)/(2 + (i-1)*F) + X/(2 +i*F)

        if T_i>T_i_1:	
            s="Case #%d: %.7f" % (t+1,T_i_1)
            break

        i+=1

    print s

