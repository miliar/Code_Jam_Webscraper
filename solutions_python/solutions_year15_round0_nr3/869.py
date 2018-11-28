case = open('small.txt')

t = int(case.readline().rstrip())

num = {'i':0,'j':1,'k':2}
table = {'i':['-1','k','-j'],'j':['-k','-1','i'],'k':['j','-i','-1'],
        '1':['i','j','k']}
def mul(a,b):
    if a[0] != '-':
        return table[a][num[b]]
    else:
        res = table[a[1]][num[b]]
        if res[0] == '-':
            return res[1]
        else:
            return '-'+ res

for c in range(t):
    l,x = list(map(int, case.readline().rstrip().split()))
    char = case.readline().rstrip()
    if len(set(char)) == 1:
        ans = 'NO'
    elif len(set(char))*x < 3:
        ans = 'NO'
    else:
        chk = ['k','j','i']
        ans = 2
        curr = chk[ans]
        prev = char[0]
        p = 1
        i = 0
        while True:
            if prev == curr and ans != 0:
                ans -= 1
                curr = chk[ans]
                if len(char) == i + 1:
                    if p < x:
                        p += 1
                        i = 0
                        prev = char[i]
                    else:
                        break
                else:
                    i = i + 1
                    prev = char[i]
            else:
                if len(char) == i + 1:
                    if p < x:
                        p += 1
                        i = 0
                        prev = mul(prev,char[i])
                    else:
                        break
                else:
                    i = i + 1
                    prev = mul(prev,char[i])
        if prev == 'k' and ans == 0:
            ans = 'YES'
        else:
            ans = 'NO'
    print('Case #{}: {}'.format(c+1,ans))
