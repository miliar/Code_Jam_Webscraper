def tidy(filename):
    f=open(filename,'rU')
    tc=int(f.readline())
    g=open('tidySmall.out','w')

    for i in range(tc):
        number=int(f.readline())
        for j in range(number,0,-1):
            if str(j)==''.join(sorted(str(j))):
                g.write(('Case #%d: %d\n')%(i+1,j))
                break
    f.close()
    g.close()

tidy('B-small-attempt0.in')
