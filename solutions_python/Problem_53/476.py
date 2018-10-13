fin = open('in.txt')
fout = open('out.txt','w')

t = int(fin.readline())
for i in range(1,t+1):
    n,k = fin.readline().split()
    #print(n,k)
    k = int(k)
    n = 2**int(n) -1
    #print(n,k)
    if k & n == n:
        fout.write("Case #{}: ON\n".format(i))
    else:
        fout.write("Case #{}: OFF\n".format(i))

fin.close()
fout.close()
