import sys

dic = {'1':1, 'i': 2, 'j': 3, 'k':4}

mat = [
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4],
    [0, 2, -1, 4, -3],
    [0, 3, -4, -1, 2],
    [0, 4, 3, -2, -1]
]

def check(L, X, string):
    str_list = list(string)
    x = 1
    x_sign = 1

    flag1, flag2 = False, False

    for i in range(L * X):
        if x_sign * x == 2:
            flag1 = True

        if x_sign * x == 4 and flag1 == True:
            flag2 = True

        c = dic[str_list[i % L]]
        x = mat[x][c]
        if x < 0:
            x_sign = -x_sign
            x = -x

    if flag1 == True and flag2 == True and x_sign * x == -1:
        return True
    else:
        return False



if len(sys.argv) < 2:
    sys.exit(1)

fin = open(sys.argv[1])
fout = open("output", 'w')

T = int(fin.readline().split()[0])

for t in range(1,T+1):
    #print(t)
    L,X = [int(x) for x in fin.readline().split()]
    string = fin.readline().split()[0]
    
    out = "YES" if check(L, X, string) else "NO"
    out_str = "Case #{0}: {1} \n".format(t, out)
    fout.write(out_str)

fin.close()
fout.close()
