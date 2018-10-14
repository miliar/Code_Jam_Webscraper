

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



'''


'''
t = int(input())  # read a line with a single integer
for b in range(1, t + 1):
    N, k = list(input().split())
    N, k = int(N), int(k)
    if N % 2 == 0:
        ls = N//2 - 1
        rs = N//2
    else:
        ls, rs = N//2, N//2

    turns = 1
    count = 2
    while(True):
        if turns >= k:
            if ls < 0: ls = 0
            if rs < 0: rs = 0
            break

        if ls == rs:
            ls = ls//2 - 1
            rs = rs//2
            
        else:
            ls = ls // 2
            rs = rs // 2

        turns += count
        count *= 2
            
        
        
        
    print("Case #{}: {} {}".format(b, ls, rs))





string = input()

length = len(string)
hf = string[:length//2][::-1]
he = string[length//2:]

if length%2 != 0:
    he = he[1:]

count = sum(hf[i] != he[i] for i in range(len(he)))

if count == 1:
    print('YES')
    
elif count < 2 and length%2 !=0:
    print('YES')
else:
    print('NO')

'''


'''
num = int(input())
f = input()
l = len(f)
moves = 0
strings = [f]
for k in range(num - 1):
    c = input()
    strings.append(c)
    count = -1
    cyc = False
    for i in range(l):
        if f == c:
            cyc = True
            break
        else:
            f = f[1:] + f[0]
            count += 1

    if not cyc:
        moves = -1
        break
    
    f = c
    
if moves == -1:
    print(moves)


else:
    moves = []
    for k in range(num):
        c = strings[k]
        countAll = 0
        for j in range(num):
            count = 0
            f = strings[j]
            
            for i in range(l):
                if f == c:
                    break
                else:
                    f = f[1:] + f[0]
                    count += 1

            countAll += count

        
        moves.append(countAll)

    print(min(moves))

'''

t = int(input())


for i in range(t):
    D, N = [int(x) for x in input().split()]
    k, s = [int(x) for x in input().split()]
    a = (D * s) / (D - k)
    for j in range(N-1):
        k, s = [int(x) for x in input().split()]
        ac = (D * s) / (D - k)
        if ac < a: a = ac

    print("Case #" + str(i+1) + ": " + str(a))



    





