import sys

def get_num_intersects(A, B):
    X = zip(A, B)
    X.sort(key = lambda x: x[0])
    num = 0
    for i, (a, b) in enumerate(X):
        for _, b2 in X[i+1:]:
            if b > b2:
                num += 1
    return num                
        

def run(f):
    case_num = int(f.readline())
    for i in xrange(case_num):
        N = int(f.readline())
        A = []
        B = []
        for _ in xrange(N):
            a, b = map(int, f.readline().split())
            A.append(a)
            B.append(b)
        print "Case #%d: %d" % (i+1, get_num_intersects(A, B))
            
if __name__ == '__main__':
    import sys
    run(open(sys.argv[1]))