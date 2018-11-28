path = '/import/grecc/ducas/gcj/'
def read_vec(str,ring=ZZ):
    cols=r.split(' ')
    v=vector(ring,[ring(x) for x in cols])
    return v
    
def read_data(filen,ring=ZZ):
    f = open(path+filen,'r')
    l = []
    for line in f.read().split('\n'):
        l+= read_vec(line,ring)        
    f.close()        
    return l

def mytranspose(b):
    bb = [[b[j][i] for j in range(4)] for i in range(4)]
    return bb

def mydiags(b):
    bb = [[b[j][j] for j in range(4)],[b[j][3-j] for j in range(4)] ]
    return bb

def prep_all_test(b):
    return b + mytranspose(b) + mydiags(b)


def test_one(v):
    X = v.count('X')
    O = v.count('O')
    T = v.count('T')
    if X+T>=4:
        return "X won" 
    if O+T>=4:
        return "O won"
    return ""


def solve(a):
    res = ""
    for v in a:
        res = test_one(v)
        if res <> "":
            return res
    for v in a:
        if v.count('.')>0:
            return "Game has not completed"
    return "Draw"
        
def read_data_ex1(filen):
    f = open(path+filen,'r')
    l = f.read().split('\n')
    f.close()
    fout = file(path+filen+".out",'w')
    
    n = ZZ(l[0])
    for i in range(n):
        a = l[1+5*i:5+5*i]
        b = [list(x) for x in a]
        bb = all_test(b)
        print >> fout, "Case #"+str(i+1)+":", solve(bb)

read_data_ex1("ex1/A-large.in")
