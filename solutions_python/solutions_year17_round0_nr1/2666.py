fin = open('1.in')
fout = open('1.out', 'w')


n = int(fin.readline())

for t in range(0, n):
    str,sk = fin.readline().split(' ')
    k = int(sk)
    flip = 0
    l = len(str)
    pan = [0 for x in range(l)]
    for i in range(0,l):
        if str[i] == '+':
            pan[i] = 1

    for i in range(0, l-k):
        if pan[i] == 0:
            print pan
            for j in range(i,i+k):
                pan[j] = 1-pan[j]
            flip += 1

    sum = 0
    
    for i in range(l-k,l):
        sum = sum + pan[i]
    
    if sum==0 or sum ==k:
        flip = flip + (sum ==0)
        fout.write("Case #%d: %d\n" %(t+1, flip))
    else:
        fout.write("Case #%d: IMPOSSIBLE\n" %(t+1))    


fin.close();
fout.close();