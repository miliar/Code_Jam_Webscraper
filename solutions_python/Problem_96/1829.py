possibilities = [set() for i in range(31)]

def is_allowed(l) :
    return max(l)-min(l) <= 2

def is_surprise(l) :
    return max(l)-min(l) == 2

def recurse(N,S,ti,listsofar,p) :
    if N==0:
        if S==0 :
            counter = 0
            global best
            for googler in listsofar :
                #print googler,p,max(googler)
                if max(googler) >= p:
                    counter+=1
            best = max(best,counter)
        return
    for poss in possibilities[ti[0]]:
        if is_surprise(poss) and S==0 :
            continue
        listsofar.append(poss)
        recurse(N-1, S-is_surprise(poss), ti[1:], listsofar,p)
        listsofar.pop()
    
    return


for i in range(11) :
    for j in range(i,11) :
        for k in range(j,11) :
            l = (i,j,k)
            t = i+j+k
            if is_allowed(l) : possibilities[t].add(l)

#for n in range(31) : print n , possibilities[n]

fin = open('in2.txt','r')
fout = open('out2.txt','w')

T = int(fin.readline())
global best

for t in range(T):
    best=0
    l = fin.readline()
    s = l.split(' ')
    N,S,p = [int(i) for i in s[0:3]]
    ti = [int(i) for i in s[3:]]
    recurse(N,S,ti,[],p)
    fout.write('Case #{}: {}\n'.format(t+1,best))





fin.close()
fout.close()

fout = open('out2.txt','r')
for l in fout : print l[:-1]
