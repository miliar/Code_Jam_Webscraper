input_file = "A-large.in"


def line(f,_type=str):
    s = [_type(i) for i in f.readline().strip().split()]
    return s


with open(input_file) as fin:
    with open('output.txt','w') as fout:
        T = line(fin,int)[0]
        for case in range(1,T+1):
            Smax,s = line(fin,str)
            a = 0
            b = 0
            for c in s:
                n = int(c)
                a += n-1
                if a < 0:
                    a += 1
                    b += 1
            print "Case #%d: %d" % (case, b)
            fout.write("Case #%d: %d\n" % (case, b))
