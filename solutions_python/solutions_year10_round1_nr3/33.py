def parse_testcase(itr):
    return parse_numbersline(itr)

def test_num(a,b):
    if b > a:
        t=b
        b=a
        a=t   
    f = True
    count = 0
    while a > b:
        if a >= 2*b:
            #print count,a,b,f
            return f
        t=b
        b=a-b
        a=t
        f = not f
        count +=1
    #print count,a,b,f
    return not f

def proc_testcase(tc):
    a1,a2,b1,b2=tc
    s=0
    for i in range(a1,a2+1):
       for j in range(b1,b2+1):
           if test_num(i,j):
               s+=1
    return str(s)

def parse_file(fstr):
    itr=iter(fstr)
    c=parse_countline(itr)
    for i in range(1,c+1):
        yield(i,parse_testcase(itr))

def parse_countline(itr):
    return int(itr.next().strip())

def parse_numbersline(itr):
    l=itr.next().strip().split()
    return tuple(map(int,l))

def main(argv):
    ifstr=open(argv[0],'rU')
    ofstr=open(argv[1],'wb')
    for i, tc in parse_file(ifstr):
        ofstr.write('Case #%d: %s\n'%(i, proc_testcase(tc)))
    ofstr.close()
    ifstr.close()

if __name__=='__main__':
    import sys
    main(sys.argv[1:])
    
