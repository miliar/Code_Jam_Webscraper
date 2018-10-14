def getPancakeSide(pancakes, K):
    flips = 0
    s = [x for x in pancakes]
    l = len(s)-K+1
    for i in range(l):
        if s[i] == '-':
            flips += 1
            for j in range(i,K+i):
                if s[j] == '-':
                    s[j] = '+'
                else:
                    s[j] = '-'
    if '-' in s:
        return 'IMPOSSIBLE'
    return flips        

with open('A-large.in','r') as f, open('outputL.txt','w') as o:
    first = True
    caseNum = 0
    for line in f:
        if first:
            first = False
            continue
        tmp = line.split()
        S = str.strip(tmp[0])
        K = int(str.strip(tmp[1]))
        result = getPancakeSide(S,K)
        o.write('Case #{0}: {1}\n'.format(caseNum+1, result))
        #print(('Case #{0}: {1}\n'.format(caseNum+1, result)))
        caseNum += 1
    #print('Done')