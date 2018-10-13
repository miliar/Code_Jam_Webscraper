
def solver(smax, ss):
    ans = 0
    
    claping = 0
    for ind, i in enumerate(ss):
        incr = 0
        if claping < ind:
            incr = ind-claping
            ans += incr
        claping += int(i) + incr
    
    return ans
    
path = "C:/Users/Panagiotis/Downloads/"
filename = "A-large"
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
    
    arr = fin.readline().rstrip('\n').split(" ")
    
    smax = arr[0]
    ss = arr[1]
    
    print(smax, ss)
    
    #N = r_int()
    #wires = [r_intArr() for _ in range(N)]
    
    #print(N, wires)
    
    print('----------------------------')
    ans = ""
    ans = solver(smax, ss)
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