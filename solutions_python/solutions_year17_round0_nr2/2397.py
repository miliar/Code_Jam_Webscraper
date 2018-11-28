fin = open('B-large.in','r')
fout = open('opt.in','w')
T = int(fin.readline())
#T=int(input())
for i in range(0,T):
    out = "case #" + str(i+1) + ": "
    #N = list(input())
    N = list(fin.readline().strip("\n"))
    N = list(map(int,N))
    l=list()
    l = sorted(N)
    j = len(N)-1
    while(l!=N):
        N[j] = 9
        N[j-1] = N[j-1] -1
        l = sorted(N)
        j = j-1
    if N[0] <=0 :
        N = N[1:]
    x = ''.join(str(e) for e in N)
    out = out+x+"\n"
    fout.write(out)
fin.close()
fout.close()
