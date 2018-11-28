def and_fn(m,n):
    return m & n


def checking_win(a,b,k):
    c = 0
    for i in range (0,a):
        for j in range(0,b):
            if (and_fn(i,j)<k):
                c+=1
    return c


def result(a,b,k,n):
    output = checking_win(a,b,k)
    return "Case #"+str(n)+": "+str(output)+"\n"


fin = open("B-small-attempt0.in","r")
fout = open("Bsmall.txt","w")
n = int(fin.readline())
for i in range (0,n):
    s = fin.readline()
    s = s.replace('\n','')
    temp = list(map(int,s.split()))
    fout.write(result(temp[0],temp[1],temp[2],i+1))
fout.close()

