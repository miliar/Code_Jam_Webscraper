import string

def oidx(i,k,N):
    k = ((N-1)-k)

    x = i-N/2
    y = k-N/2
    if N%2==0:#even case
        if x>=0:
            x+=1
        if y>=0:
            y+=1

    #rotation. 90d
    xx = -y
    yy = x
    
    #restore original coordi
    if N%2==0:#even case
        if xx>=0:
            xx-=1
        if yy>=0:
            yy-=1
    xx+= N/2
    yy+= N/2
    xx = ((N-1)-xx)

    return (xx,yy)

ifile = open("A-large.in")
#ifile = open("A-small-attempt0.in")
file_s = ifile.read().split("\n")
ifile.close()

T = int(file_s[0])

out = []

NKidx = 1

for t in range(0,T):
    NKline = file_s[NKidx]
    N = int(NKline.split(" ")[0])
    K = int(NKline.split(" ")[1])
#    print N,K#dbg
#    print oidx(6,6,N)
#    print oidx(0,0,N)
    
    #create board
    B = []
    for i in range(0,N):
        B.append(list(file_s[NKidx+i+1]))
    #rotate board(clockwise = -90d)
    R=[]
    for i in range(0,N):
        R.append(['x']*N)
    for i in range(0,N):
        for k in range(0,N):
            oi,ok = oidx(i,k,N)
            R[i][k] = B[oi][ok]

    
    #gravity
    drop=[N-1]*N
    for i in range(N-1,-1,-1):
        for k in range(0,N):
            if not R[i][k]==".":
                if not drop[k]==i:
                    R[drop[k]][k] = R[i][k]
                    R[i][k] = "."
                drop[k] -= 1
    
    #find K row
    d = dict()
    d['R'] = False
    d['B'] = False
    d['.'] = False
    for i in range(0,N):
        for k in range(0,N):
            is_v= True
            is_h= True
            is_d= True
            is_d2= True
            if i<=N-K:#vertical
                for m in range(0,K):
                    if not R[i+m][k]==R[i][k]:
                        is_v = False
                if is_v:
                    d[R[i][k]] = True
            if k<=N-K:#horiz
                for m in range(0,K):
                    if not R[i][k+m]==R[i][k]:
                        is_h = False
                if is_h:
                    d[R[i][k]] = True
            if i<=N-K and k<=N-K:#dia
                for m in range(0,K):
                    if not R[i+m][k+m]==R[i][k]:
                        is_d = False
                if is_d:
                    d[R[i][k]] = True
            if i<=N-K and -1<=k-K:#dia2
                for m in range(0,K):
                    if not R[i+m][k-m]==R[i][k]:
                        is_d2 = False
                if is_d2:
                    d[R[i][k]] = True

    #return
    if d['R'] and d['B']:
        ret_str = "Both"
    elif d['R']:
        ret_str = "Red"
    elif d['B']:
        ret_str = "Blue"
    else:
        ret_str = "Neither"
        
    out.append("Case #"+str(t+1)+": "+ret_str)
    NKidx+= (N+1)

ofile = open("output.txt","w")
ofile.write(string.join(out,"\n"))
ofile.close()