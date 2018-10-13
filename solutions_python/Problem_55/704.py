#python3
f = open("./C-small-attempt0.in")
out = open("./C-small.out","w")
times = int(f.readline().strip())
for i in range(times):
    R,size,N = [int(x) for x in f.readline().strip().split()]
    g = [int(x) for x in f.readline().strip().split()][0:N]
    index = start = 0
    maxend = N-1
    M = 0
    empty = size
    startlist = {}
    while R>0:
        if start==index and start in startlist:
            R -= 1
            M += startlist[start]['M']
            index  = startlist[start]['index']
            maxend = (index-1)%N
            start  = index
            empty  = size
        elif empty<g[index] or maxend==index:
            if empty>=g[index]:
                empty -= g[index]
                M     += g[index]
                index  = (index+1)%N
            R -= 1
            maxend = (index-1)%N
            startlist[start] = {'M':size-empty,'index':index}
            start  = index
            empty  = size
        else:
            empty -= g[index]
            M     += g[index]
            index  = (index+1)%N
    #print(startlist)
    out.write("Case #%s: %s\n"%(i+1, M));
    
f.close()
out.close()
