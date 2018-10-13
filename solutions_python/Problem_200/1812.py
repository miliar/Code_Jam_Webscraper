fin = open("B.in")
fout = open("B.out","w")

t = int(fin.readline())

def tidy(x):
    for i in range(1,len(x)):
        if int(x[i-1]) > int(x[i]):
            return False
    return True

for trial in range(1,t+1):
    N = fin.readline().strip()
    suffix = ''
    while not tidy(N):
        while len(N) > 1 and N[-1] == '9':
            suffix += '9'
            N = N[:-1]
        N = str(int(N)-1)
    res = N+suffix
    # --------------------------------------------------------------------------
    print("Case #"+str(trial)+": "+res)
    fout.write("Case #"+str(trial)+": "+res+'\n')
