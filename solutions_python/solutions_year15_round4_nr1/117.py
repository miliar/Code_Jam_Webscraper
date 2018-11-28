import sys
sys.stdin = open('A-large.in')
sys.stdout = open('out.txt', 'w')

def val(s):
    if s=='.': return -1
    if s=='>': return 0
    if s=='^': return 1
    if s=='<': return 2
    if s=='v': return 3

n_cases = int(input())
for case in range(n_cases):
    print(case, end=' ', file=sys.stderr)
    r,c = list(map(int, input().split()))
    a = [[0]*c for i in range(r)]
    for i in range(r):
        s = input()
        for j in range(c):
            a[i][j] = val(s[j])
    ok = True
    for i in range(r):
        j0 = -1
        total = 0
        for j in range(c):
            if a[i][j] != -1:
                total += 1
                j0 = j
        if total == 1:
            total_in_col = 0
            for ii in range(r):
                if a[ii][j0] != -1:
                    total_in_col += 1
            ok &= total_in_col > 1
    if ok:
        res = 0
        for i in range(r):
            j=0
            while j<c and a[i][j] == -1:
                j += 1
            if j<c and a[i][j]==2: res += 1

            j=c-1
            while j>=0 and a[i][j] == -1:
                j -= 1
            if j>=0 and a[i][j]==0: res += 1

        for j in range(c):
            i=0
            while i<r and a[i][j] == -1:
                i += 1
            if i<r and a[i][j]==1: res += 1

            i=r-1
            while i>=0 and a[i][j] == -1:
                i -= 1
            if i>=0 and a[i][j]==3: res += 1
    else:
        res = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(case+1, res))

print(file=sys.stderr)

