import sys,os

class OutFile(file):
    def __init__(self,file_name):
        file.__init__(self,file_name,'w')
    def write(self,x):
        sys.stdout.write(x)
        file.write(self,x)
    def writelines(self,x):
        print x
        assert False
    def __enter__(self,*argv):
        return self
    def __exit__(self,*argv):
        self.close()

def do(file_name):
    name,ext = os.path.splitext(file_name)
    file_out = name+'.out'
    with open(file_name) as f1:
        with OutFile(file_out) as f2:
            case = int(f1.readline())
            for i in xrange(case):
                print >>f2,'Case #%d:'%(i+1),
                calculate(f1,f2)

def sqrt(I):
    S,S1 = I,I+1
    while S < S1:
        S,S1 = (S+I/S)/2,S
    return S1

def rev(n):
    N1 = str(n)
    N2 = N1[::-1]
    return N1==N2

def calculate(f_in,f_out):
    start,end = map(int,f_in.readline().split())
    st_ro,en_ro = sqrt(start),sqrt(end)
    while st_ro*st_ro < start:
        st_ro+=1
    while (en_ro+1)*(en_ro+1)<=end:
        en_ro+=1
    count=0
    for num in xrange(st_ro,en_ro+1):
        if rev(num) and rev(num*num):
            count+=1
    print >>f_out,count

if __name__ == '__main__':
    do(sys.argv[1])
