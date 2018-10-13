import time
def mod(lawn,check,n,m):
    for i in range(n):
        for j in range(m):
            #print i,j,i*n+j
            if check[i*m+j] == True:
                continue
            a = [lawn[i][k] for k in range(m)]
            b = [lawn[k][j] for k in range(n)]
            if max(a) <= lawn[i][j]:
                check[i*m+j] = True
                continue
            if max(b) <= lawn[i][j]:
                check[i*m+j] = True
                continue
            return 0
    return 1
        


f = open('B-large.in','r')
g = open('B-large-output.out','w')
start_time = time.time()
test = int(f.readline())
for x in range(test):
    temp = (f.readline()).split(' ')
    dim = map(int,temp)
    lawn=[]
    for i in range(dim[0]):
        temp2 = (f.readline()).split(' ')
        lawn.append(map(int,temp2))
    #print dim[0],dim[1],lawn
    check = [False]*(dim[0]*dim[1])
    ##########################
    ret = mod(lawn,check,dim[0],dim[1])
    if ret == 0:
        writ = 'Case #'+str(x+1)+': NO'
    elif ret == 1:
        writ = 'Case #'+str(x+1)+': YES'
    g.write(writ)
    g.write('\n')
    ##########################
f.close()
g.close()
print time.time()-start_time
