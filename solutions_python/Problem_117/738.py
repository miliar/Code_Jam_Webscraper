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

def cut_row(glass,h,th):
    for th1 in xrange(len(glass[0])):
        glass[th][th1] = min(glass[th][th1],h)
def cut_col(glass,h,th):
    for th1 in xrange(len(glass)):
        glass[th1][th] = min(glass[th1][th],h)

def calculate(f_in,f_out):
    h,w = map(int,f_in.readline().split())
    glass = []
    for i in xrange(h):
        glass.append(map(int,f_in.readline().split()))
    glass_ = [[100 for j in xrange(w)] for i in xrange(h)]
    for i,row in enumerate(glass):
        M = max(row)
        cut_row(glass_,M,i)
    for j,col in enumerate(zip(*glass)):
        M = max(col)
        cut_col(glass_,M,j)
    print >>f_out,'YES' if glass == glass_ else 'NO'

if __name__ == '__main__':
    do(sys.argv[1])
