

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


'''
'''   
t = int(input())


for i in range(t):
    N, R, O, Y, G, B, V = [int(x) for x in input().split()]

    circ = ['' for x in range(N)]

    if Y != 0: ys = N // Y
    if B != 0: bs = N // B
    if R != 0: rs = N // R

    if R == max(Y,R,B):
        f = R
        first = 'R'
        Rs = rs
        if B >= Y:
            s = B
            g = Y
            Ys = bs
            Bs = ys
            second = 'B'
            third = 'Y'
        else:
            s = Y
            g = B
            Ys = ys
            Bs = bs
            second = 'Y'
            third = 'B'


    elif B == max(Y,R,B):
        first = 'B'
        f = B
        Rs = bs
        if R >= Y:
            s = R
            g = Y
            Ys = rs
            Bs = ys
            second = 'R'
            third = 'Y'
        else:
            s = Y
            g = R
            Ys = ys
            Bs = rs
            second = 'Y'
            third = 'R'

    else:
        first = 'Y'
        f = Y
        Rs = ys
        if R >= B:
            s = R
            g = B
            Ys = rs
            Bs = bs
            second = 'R'
            third = 'B'

        else:
            s = B
            g = R
            Ys = bs
            Bs = rs
            second = 'B'
            third = 'R'
 
    idx = 0
    j = 0
    while j < f:
        if '' not in circ: break
        if circ[(idx + j * Rs) % N] != '':
            idx = circ.index('')
            j = 0
            continue
        circ[idx + j * Rs % N] = first
        j += 1
    
    if '' in circ:
        idx = circ.index('')
        j = 0
        c = 0
        while c < s:
            if '' not in circ: break
            if circ[(idx + j * Ys) % N] != '':
                idx = (idx + j * Ys)%N + 1
                j = 0
                continue
            circ[idx + j * Ys % N] = second
            c += 1
            j += 1

        if '' in circ:
            idx = circ.index('')
            j = 0
            c = 0
            while c < g:
                if '' not in circ: break
                if circ[(idx + j * Bs) % N] != '':
                    idx = (idx + j * Bs) % N + 1
                    j = 0
                    continue
                circ[idx + j * Bs % N] = third
                j += 1
                c += 1

    circ = [x for x in ''.join(circ)]

    impossible = False
    if circ[-1] == circ[0] or circ[1] == circ[0]:
        impossible = True
        print("Case #" + str(i+1) + ": IMPOSSIBLE")

    elif circ[-1] == circ[0] or circ[-1] == circ[-2]:
        impossible = True
        print("Case #" + str(i+1) + ": IMPOSSIBLE")
        
    else:
        for j in range(1, N-1):
            if circ[j] == circ[j-1] or circ[j] == circ[j+1]:
                impossible = True
                print("Case #" + str(i+1) + ": IMPOSSIBLE")
                break
    
    if not impossible:
        print("Case #" + str(i+1) + ": " + ''.join(circ))



'''
'''
import math as math

t = int(input())


for i in range(t):
    N, k = [int(x) for x in input().split()]
    h = []
    r = []
    maxIndex = 0
    maxR = 0
    maxH = 0
    for j in range(N):
        rj, hj = [int(x) for x in input().split()]
        print(math.pi*(2*rj*hj + rj**2))
        if (2*rj*hj + rj**2  > 2*maxR*maxH + maxR**2):
            maxR = rj
            maxH = hj
            maxIndex = j        
        h.append(hj)
        r.append(rj)

    del h[maxIndex]
    del r[maxIndex]
    
    k = k - 1
    hr = [a*b for a,b in zip(h,r)]
    hr = sorted(hr)
    for a in hr: print(2*math.pi*a)
    
    result = math.pi*(maxR**2 + 2*(sum(hr[len(hr)-k:]) + maxR*maxH))
    
    print("Case #" + str(i+1) + ": " + str(result))
        
    

'''



t = int(input())
for i in range(t):
    Ac, Aj = [int(x) for x in input().split()]

    if ((Ac == 1 and Aj == 0) or (Ac == 0 and Aj == 1)):
        a1s, a1f = [int(x) for x in input().split()]
        print("Case #" + str(i+1) + ": " + str(2))

    elif (Ac == 1 and Aj == 1):
        a1s, a1f = [int(x) for x in input().split()]
        a2s, a2f = [int(x) for x in input().split()]
        print("Case #" + str(i+1) + ": " + str(2))

    else:
        a1s, a1f = [int(x) for x in input().split()]
        a2s, a2f = [int(x) for x in input().split()]

        if(a1s < a2s):
            res = min(abs(a2f-a1s), abs(a1f+1440-a2s))
        else:
            res = min(abs(a1f-a2s), abs(a2f+1440-a1s))
            
        if(res > 720):
            print("Case #" + str(i+1) + ": " + str(4))

        else:
            print("Case #" + str(i+1) + ": " + str(2))


    













