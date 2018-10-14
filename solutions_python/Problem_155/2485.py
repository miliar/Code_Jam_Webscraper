outf = open('out-large.txt', 'w')
with open('A-large.in') as f:
    w = [int(x) for x in f.readline().split()]
    lineno = 1
    for line in f:
        a = [x for x in line.split()]
        sofar = 0
        friends = 0
        required = 0
        b = [int(x) for x in a[1]]
        for idx, val in enumerate(b):
            if(sofar < idx):
                required += (idx - sofar)
                sofar += (idx - sofar)
            sofar += val
        outf.write("Case #%d: %d\n" %(lineno, required))
        lineno +=1
                 
            
    