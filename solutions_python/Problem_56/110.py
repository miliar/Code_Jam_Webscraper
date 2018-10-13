T=int(input())


def check0(b, K, c):
    for row in b:
        n=0
        for r in row:
            if r == c:
                n+=1
                if n==K:
                    return True
            else:
                n=0
def check1(b, K, c):
    for i in range(0, len(b)):
        n=0
        for j in range(0, len(b)):
            if b[j][i] == c:
                n+=1
                if n==K:
                    return True
            else:
                n=0
    return False

def check2(b, K, c):
    N=len(b)
    for i in range(0,N):
        n=0
        for k in range(0,N - i):
            if b[i+k][k] == c:
                n+=1
                if n==K:
                    return True
            else:
                n=0
    for i in range(1, N):
        n=0
        for k in range(0,N - i):
            if b[k][i+k] == c:
                n+=1
                if n==K:
                    return True
            else:
                n=0
    return False

def check3(b, K, c):
    N=len(b)
    for i in range(0,N):
        n=0
        for k in range(0,N - i):
            if b[N - 1 - (i+k)][k] == c:
                n+=1
                if n==K:
                    return True
            else:
                n=0
    for i in range(1, N):
        n=0
        for k in range(0,N - i):
            if b[N - 1 - k][i+k] == c:
                n+=1
                if n==K:
                    return True
            else:
                n=0
    return False

def check(b, K, c):
    return check0(b,K,c) or check1(b,K,c) or check2(b,K,c) or check3(b,K,c)

for t in range(0,T):
    line=input().split()
    N=int(line[0])
    K=int(line[1])
    
    b=[]
    for n in range(0,N):
        line = [c for  c in input()]
        i=N-1
        row=[]
        while i >= 0:
            if line[i] != '.':
                row.append(line[i])
            i-=1

        while len(row) < N:
            row.append('.')

        b.append(row)

    result='Neither'
    if check(b, K, 'R'):
        if check(b,K,'B'):
            result='Both'
        else:
            result='Red'
    elif check(b,K,'B'):
        result='Blue'

    print('Case #{0}: {1}'.format(t+1, result))
