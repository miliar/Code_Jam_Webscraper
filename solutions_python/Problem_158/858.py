
def solver(X, R, C):
    
    RC = R*C
    minrc = min([R, C])
    maxrc = max([R, C])
        
    if RC < X:
        return 'RICHARD'
    if X > maxrc:
        return 'RICHARD'
    if not RC%X == 0:
        return 'RICHARD'
    
    if X%2 == 0:
        f = (X)/2
    else:
        f = (X-1)/2 + 1
    
    if f > minrc:
        return 'RICHARD'
    
    if minrc > 1: 
        if ((minrc-1)*(minrc+1)+1) <= X:
            return 'RICHARD'
    
    return 'GABRIEL'

    
path = "C:/Users/Panagiotis/Downloads/"
filename = "D-small-attempt1"
fin = open(path + filename + ".in", "r")
fout = open(path + filename + ".out", "w")

# Per-line read functions
def r_int():
    x = int(fin.readline())
    return x

def r_intArr():
    arr = fin.readline().rstrip('\n').split(" ")
    return [int(e) for e in arr]

def r_intTup():
    arr = fin.readline().rstrip('\n').split(" ")
    return tuple(int(e) for e in arr)
def r_floatTup():
    arr = fin.readline().rstrip('\n').split(" ")
    return tuple(float(e) for e in arr)

def r_int_intArr():
    arr = fin.readline().rstrip('\n').split(" ")
    return (int(arr[0]), [int(e) for e in arr[1:]])

def r_line():
    s = fin.readline().rstrip('\n')
    return s

# Multi-line read functions
def r_intMat(n):
    mat = []
    for _ in range(n):
        arr = fin.readline().rstrip('\n').split(" ")
        mat.append([int(e) for e in arr[0:]])
    return mat

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------

T = r_int()
for i in range(T):

    (X, R, C) = r_intTup()
    print(X, R, C)
    
    #N = r_int()
    #wires = [r_intArr() for _ in range(N)]
    
    #print(N, wires)
    
    print('Case ', i+1, '----------------------------')
    ans = ""
    ans = solver(X, R, C)
    print('----------------------------')
    
    '''
    fout.write("Case #" + str(i+1) + ":")
    for i in ans:
        fout.write("\n")
        for ind, j in enumerate(i):
            if ind > 0:
                fout.write(" ")
            fout.write(str(j))
    fout.write("\n")
    '''
    #ans = str("%04d" % (ans,))
    #ans = str('%.7f' % ans)
    ans = str(ans)
    fout.write("Case #" + str(i+1) + ": " + ans + "\n")
     
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------   