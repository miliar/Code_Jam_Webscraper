def checkrow(ind,jnd, n ,m):
    for k in xrange(m):
        if(int(a[ind][k]) !=1):
            return False
    return True
def checkcol(ind,jnd, n ,m):
    for k in xrange(n):
        if(int(a[k][jnd]) !=1):
            return False
    return True

T =  int(raw_input())
a = []
for testcase in xrange(T):
    a = []
    nm = (raw_input()).split(' ')
    n = int(nm[0])
    m = int(nm[1])
    sucess = True
    for rows in range(n):
        row = (raw_input()).split(' ')
        a.append(row)
    for i in xrange(n):
        for j in xrange(m):
            if int(a[i][j]) == 1:
                if(not (checkrow(i,j , n,m) or checkcol(i,j , n,m) )):
                    sucess = False
                    break
        if(not sucess):
            print("Case #"+str(testcase+1)+": NO")
            break
    if (sucess):
        print("Case #"+str(testcase+1)+": YES")
