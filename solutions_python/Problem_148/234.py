# ?

#file_in = "A-sample.in"
#file_out = "A-sample.out"
file_in = "A-small-attempt0.in"
file_out = "A-small-attempt0.out"
#file_in = "A-large.in"
#file_out = "A-large.out"

# Solves the problem
def Solve(N, X, fs):
    fs = sorted(fs)
    res = 0
    while(0 < len(fs)):
        l = fs[-1]
        fs.remove(l)
        RemoveNotGreater(fs, X - l)
        res = res + 1
    return res

def RemoveNotGreater(fs, v):
    if 0 == len(fs):
        return False
    for vv in range(v, 0, -1):
        if vv in fs:
            fs.remove(vv)
            return True
        if fs[0] >= vv:
            return False
    return False

# Reads the input data and runs the test cases
def Run():
    fin = open(file_in, 'r')
    fout = open(file_out, 'w')

    lines = []
    for l in fin:
        lines.append(l)

    i = 0
    T = int(lines[0])
    i = i + 1
    
    for tc in range(0, T):
        NX = lines[i].rstrip().split(' ')
        i = i + 1
        N, X = int(NX[0]), int(NX[1])
        fs = []
        fss = lines[i].rstrip().split(' ')
        i = i + 1
        for j in range(0, N):
            fs.append(int(fss[j]))
        result = str(Solve(N, X, fs))
        fout.write("Case #" + str(tc + 1) + ": " + result + '\n')
    fin.close()
    fout.close()
    

def main():
    Run()

if __name__ == "__main__":
    main()
