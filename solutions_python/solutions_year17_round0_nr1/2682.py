

'''
t = int(input())  # read a line with a single integer
for b in range(1, t + 1):
    
    n = list(input())
    eqInd = 0
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            n[eqInd] = str(int(n[eqInd]) - 1)
            n[eqInd + 1:] = ['9'] * (len(n) - eqInd - 1)
            break
        
        if n[i] == n[eqInd]:
            continue
        elif n[i] == n[i-1]:
            eqInd = i - 1
            continue
        else:
            eqInd = i
            
    if n[0] == '0': n = n[1:]
                   
    print("Case #{}: {}".format(b, ''.join(n)))
'''


t = int(input())  # read a line with a single integer
for b in range(1, t + 1):
    panc, k = list(input().split())
    k = int(k)
    moves = 0
    lastP = 'B'
    while(True):
        if lastP == panc:
            break
        lastP = panc
        panc = panc.rstrip('+').lstrip('+')
        while(k <= len(panc) and panc[:k] == '-'*k):
            panc = panc[k:]
            moves += 1
        while(k <= len(panc) and panc[len(panc)-k:] == '-'*k):
            panc = panc[:len(panc)-k]
            moves += 1

        if panc == '':
            break
        
        if panc[0] == '-' and panc[-1] == '-':
            fp = panc.find('+')
            if fp == -1:
                continue
            p = list(panc)
            while fp < k and fp + k <= len(panc):
                p[fp:fp + k] = list(panc[fp:fp + k].replace('-', '1').replace('+','-').replace('1','+'))
                panc = ''.join(p)
                fp = panc.find('+')
                moves += 1
                if(fp == -1):
                    break
        
    panc = panc.rstrip('+').lstrip('+')
    if panc == '':
        print("Case #{}: {}".format(b, moves))
    else:
        print("Case #{}: {}".format(b, 'IMPOSSIBLE'))


















