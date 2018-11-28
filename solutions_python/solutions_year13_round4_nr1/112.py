import sys,os,time

class OutFile(file):
    def __init__(self,file_name):
        file.__init__(self,file_name,'w')
        self.console = sys.stdout
    def __enter__(self,*argv):
        sys.stdout = self
        return self
    def __exit__(self,*argv):
        sys.stdout = self.console
    def write(self,x):
        self.console.write(x)
        file.write(self,x)

class InFile(file):
    def get_int(self):
        return int(self.readline())
    def get_line_int(self):
        return map(int,self.get_line_str())
    def get_line_str(self):
        return self.readline().split()

def do_all(file_name):
    file_name1 = os.path.splitext(file_name)[0]+'.out'
    start = time.clock()
    with InFile(file_name) as f1:
        with OutFile(file_name1) as f2:
            for i in xrange(1,f1.get_int()+1):
                print 'Case #%s:'%i,
                calculation(f1)
    print time.clock() - start,'seconds'

def calculation(f_in):
    N,M = f_in.get_line_int()
    ticket = []
    normal = 0
    pay = lambda n:(N*n-n*(n-1)/2)
    for i in xrange(M):
        s,o,p = f_in.get_line_int()
        ticket.append((s,False,p))
        ticket.append((o,True,p))
        normal += pay(o-s)*p
    stack = []
    ticket.sort()
    tricky = 0
    for pos,state,many in ticket:
        if not state:
            stack.append((pos,many))
        else:
            while many:
                P,M = stack.pop()
                if many <= M:
                    tricky += pay(pos-P)*many
                    M-=many
                    if M:stack.append((P,M))
                    many = 0
                else:
                    many -= M
                    tricky += pay(pos-P)*M
    assert len(stack) == 0
    print normal - tricky

if __name__ == '__main__':
    do_all(sys.argv[1])
