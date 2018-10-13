welcome = 'welcome to code jam'
#infile = open("/Users/simple/Desktop/c.txt")
#infile = open('/Users/simple/Desktop/C-small-attempt0.in')
infile = open('/Users/simple/Desktop/C-large.in')
N = int( infile.readline().strip() )
for i in range(N):
    line = infile.readline().strip()
    result = 0
    candidates = []
    for j, c in enumerate(welcome):
        if j==0:
            for k  in range(len(line)):
                if c == line[k]:
                    candidates.append( (k,1))
        else:
            old = candidates
            candidates = []
            for k  in range(len(line)):
                if c == line[k]:
                    #print(c,k)
                    v = 0
                    for cand in old:
                        if cand[0] < k:
                            v += cand[1]
                    if v > 0:
                        candidates.append( (k, v))

    #print(j,c, candidates)
    result = 0
    for cand in candidates:
        result += cand[1]
    print('Case #{}: {}'.format(i+1,str(result)[-4:].zfill(4)))
    #print('Case #{}: {:04}'.format(i+1,result))

        
    

