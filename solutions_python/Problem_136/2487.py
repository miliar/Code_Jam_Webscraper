with open('input1.in') as f:
    lines = f.readlines()

with open('output1.out', 'w') as output:
    N = int(lines[0])
    for i in xrange(1,N+1):
        C,F,X = map(float,lines[i].split(' '))
        # print C,F,X
        n = 2
        cond=True
        sum=0
        while cond:
            a = X/n
            b = (C/n)
            c =  X/(n+F)
            d = b+c
            n = n+F
            # print a,d
            if a<d:
                sum+=a
                break
            sum+=b
        output.write('Case #'+str(i)+': '+str(sum)+'\n')
        # output.write("Case #%d: %d" % (testcase+1, alone))
