'''
Created on 2010-05-21

@author: lawford
'''

def do_counts_ldown(k, X, Xcnt, rowdir, coldir, n):
    half = n
    for i in range(0,half):
        for j in range(0,half):
            miss = False
            Xcnt[i][j] = 0
            if (j-coldir < 0):
                miss = True
            if (j-coldir >= n):
                miss = True

            if (i-rowdir < 0):
                miss = True
            if (i-rowdir >= n):
                miss = True
#            if ()
            if (X[j][n-i-1] == 'x'):
                if miss:
                    Xcnt[i][j] = 1
                else:
                    Xcnt[i][j] = Xcnt[i-rowdir][j-coldir]+1
                    if (Xcnt[i][j] == k):
                         return True
    return False


def do_counts_rup(k, X, Xcnt, rowdir, coldir, n):
    half = n
    for i in range(half-1,-1,-1):
        for j in range(half-1,-1,-1):
            miss = False
            Xcnt[i][j] = 0
            if (j-coldir < 0):
                miss = True
            if (j-coldir >= n):
                miss = True

            if (i-rowdir < 0):
                miss = True
            if (i-rowdir >= n):
                miss = True
#            if ()
            if (X[j][n-i-1] == 'x'):
                if miss:
                    Xcnt[i][j] = 1
                else:
                    Xcnt[i][j] = Xcnt[i-rowdir][j-coldir]+1
                    if (Xcnt[i][j] == k):
                         return True
    return False

def do_counts_lup(k, X, Xcnt, rowdir, coldir, n):
    half = n
    for i in range(half-1,-1,-1):
        for j in range(0,half):
            miss = False
            Xcnt[i][j] = 0
            if (j-coldir < 0):
                miss = True
            if (j-coldir >= n):
                miss = True

            if (i-rowdir < 0):
                miss = True
            if (i-rowdir >= n):
                miss = True
#            if ()
            if (X[j][n-i-1] == 'x'):
                if miss:
                    Xcnt[i][j] = 1
                else:
                    Xcnt[i][j] = Xcnt[i-rowdir][j-coldir]+1
                    if (Xcnt[i][j] == k):
                         return True
    return False

def do_counts_rdown(k, X, Xcnt, rowdir, coldir, n):
    half = n
    for i in range(0,half):
        for j in range(half-1,-1,-1):
            miss = False
            Xcnt[i][j] = 0
            if (j-coldir < 0):
                miss = True
            if (j-coldir >= n):
                miss = True

            if (i-rowdir < 0):
                miss = True
            if (i-rowdir >= n):
                miss = True
#            if ()
            if (X[j][n-i-1] == 'x'):
                if miss:
                    Xcnt[i][j] = 1
                else:
                    Xcnt[i][j] = Xcnt[i-rowdir][j-coldir]+1
                    if (Xcnt[i][j] == k):
                         return True
    return False

def ck(a, b, n, k):
    for i in range(0,n):
        for j in range(0,n):
            if a[i][j]+b[i][j]-1 >= k:
                return True
    return False

def xworks(X,Xc,n,kk):
    return \
        do_counts_ldown(kk, X, Xc[0], 1, 0, n) or \
            do_counts_rdown(kk, X, Xc[1], 1, -1, n) or \
                do_counts_rup(kk, X, Xc[2], 0, -1, n) or \
                    do_counts_rup(kk, X, Xc[3], -1, -1, n) or \
                        do_counts_rup(kk, X, Xc[4], -1, 0, n) or \
                            do_counts_lup(kk, X, Xc[5], -1, 1, n) or \
                                do_counts_ldown(kk, X, Xc[6], 0, 1, n) or \
                                    do_counts_ldown(kk, X, Xc[7], 1, 1, n)


def alg(n,kk,lines):
    red = [[] for i in range(0,n)]
    blue = [[] for i in range(0,n)]
    
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if lines[i][j] == 'R':
                red[i].append('x')
                blue[i].append('o')
            if lines[i][j] == 'B':
                blue[i].append('x')
                red[i].append('o')
#            if lines[i][j] == '.':
#                blue[i].append('.')
#                red[i].append('.')

    for i in range(0,n):
        for j in range(len(red[i]),n):
            red[i].append('.')

    for i in range(0,n):
        for j in range(len(blue[i]),n):
            blue[i].append('.')


    redcnt = [ [[-1 for k in range(0,n)] for i in range(0,n)] for j in range(0,8)]
    bluecnt = [ [[-1 for k in range(0,n)] for i in range(0,n)] for j in range(0,8)]

#    half = n/2+1


    redworks = xworks(red,redcnt,n,kk)
    print("RED:"+str(redworks)+":"+str(kk))

    blueworks = xworks(blue,bluecnt,n,kk)
    print("BLUE:"+str(blueworks)+":"+str(kk))

    if not redworks and not blueworks:
         return "Neither"
    if redworks and not blueworks:
         return "Red"
    if blueworks and not redworks:
         return "Blue"
    if redworks and blueworks:
         return "Both"
#    print(lines)
#    for i in range(0,n):
#        print red[i]
#    print()
#    for i in range(0,n):
#        print blue[i]
#    
#    print("red")
#    for cnt in range(0,8):
#        for i in range(0,n):
#            print(redcnt[cnt][i])
#        print()
#
#    print("blue")
#    for cnt in range(0,8):
#        for i in range(0,n):
#            print(bluecnt[cnt][i])
#        print()
#    
#    return "done"

if __name__ == '__main__':
    fname = "A-large"
    f = open(fname+".in.txt", "r")
    f.readline()
    cnt=1
    fout = open(fname+".out.txt", "w")

    piece1 = f.readline().split(" ")
    while piece1 != ['']:
        print("piece1"+str(piece1))
        [n,k]= map(int, piece1)
        print("n:"+str(n)+" k:"+str(k))
        lines = []
        for i in range(0,n):
            lines.append(f.readline())
        result = alg(n,k, lines)
#        fout.write("Case #"+str(cnt)+": "+" ".join(result)+"\n")
        fout.write("Case #"+str(cnt)+": "+result+"\n")
        piece1 = f.readline().split(" ")
        cnt = cnt+1
    fout.close()
    f.close()
