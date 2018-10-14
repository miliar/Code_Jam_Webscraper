## flip pancake

f= open('A-large.in','r')
fout = open('A-large-result.txt','w')

casenum = int(f.readline())
for p in range(casenum):
    info = f.readline()
    s = info.split(' ') [0]
    n = len(s)
    k = int(info.split(' ') [1])

    lst = []

    for char in s:
        if char == '-':
            lst.append(-1)
        elif char == '+':
            lst.append(1)

    cnt = 0

    while -1 in lst[:(n-k+1)] :
    
        cake_to_flip = lst.index(-1)

        for i in range(k):
            lst[cake_to_flip+i] *= -1
        cnt += 1
        
    if -1 in lst:
        result = 'Impossible'
    else:
        result = str(cnt)
    output = 'Case #' + str(p+1)+': '+result
    fout.write(output)
    fout.write('\n')

fout.close()