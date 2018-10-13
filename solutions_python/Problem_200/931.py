def getPos(n,i):
    return (n/(10**i))%10

def lenInt(n):
    l = 0
    while n != 0:
        l = l+1
        n = n/10
    return l

def bruteforce(n):
    
    tidy_num = 0
    for i in range(1,n+1):
        is_tidy = True
        for j in range(0,lenInt(i)-1):
            if getPos(i,j) < getPos(i,j+1):
                is_tidy = False
                break
        if is_tidy:
            tidy_num = i
    return tidy_num

fin = open('./B-large.in','r')
fout = open('./outputB.txt','w')

t = int(fin.readline())
for i in range(0,t):
    n = fin.readline()
    n = int(n)
    n_t = 0
    idx = 0
    for j in range(0,lenInt(n)-1):
        if getPos(n,j) < getPos(n,j+1):
            idx = j+1
        elif getPos(n,j) == getPos(n,j+1) and idx == j and idx != 0:
            idx = j+1
    if idx != 0:
        n_t = (n / (10**(idx))) * (10**(idx))
        n_t = n_t - 1
    else:
        n_t = n
    #if bruteforce(n)!=n_t:
        #print n,bruteforce(n),n_t
    
    fout.write('Case #{}: {}\n'.format(i+1,n_t))
fin.close()
fout.close()
