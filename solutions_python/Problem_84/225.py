def check_tile():
    try:
        if A[j][i+1] == "#" and A[j+1][i] == "#" and A[j+1][i+1] == "#":
            return True
    except:
        return False

def replace_tile():
    A[j][i] = '/'
    A[j][i+1] = '\\'
    A[j+1][i] = '\\'
    A[j+1][i+1] = '/'

fp = open('in')
T = int(fp.readline())

for t in range(T):
    R, C = map(int,fp.readline().split())
    A = []
    for r in range(R):
        L = list(fp.readline().strip())
        A.append(L)
    # A[y][x]
    possible = True

    for j in range(R):
        for i in range(C):
            if A[j][i] == "#" and possible:
                if check_tile() :
                    replace_tile()
                else:
                    possible = False

    print "Case #%d:"%(t+1)

    if possible:
        for j in range(R):
            L = ''
            for i in range(C):
                L+=A[j][i]
            print L
    else:
        print "Impossible"


