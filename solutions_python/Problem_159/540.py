from macpath import curdir

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
for iii in range(T):

    N = r_int()    
    mushes = r_intArr()
    
    diffs = []
    for i in range(1, N):
        diff = mushes[i-1] - mushes[i]
        if diff >= 0:
            diffs.append(diff)
        else:
            diffs.append(0)
    
    y = sum(diffs)
    
    rate = max(diffs)
    z = 0
    
    print(rate)
    print(mushes)
    for i in range(0, N-1):
        if mushes[i] <= rate:
            z += mushes[i]
        else:
            z += rate
        print(i, z)
    
    z = str(z)
    y = str(y)
    fout.write("Case #" + str(iii+1) + ": " + y + " " + z + "\n")
     
# ------------------------------------------------------------------------
# ------------------------------------------------------------------------   