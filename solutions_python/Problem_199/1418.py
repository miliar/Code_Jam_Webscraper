import copy
cases = []

with open('A-large.in','r') as infile:
    for row in infile:
        paras = row.strip().split(' ')
        #print paras
        if len(paras) > 1:
            cases.append((paras[0],paras[1]))

def check_plus(n):
    for ch in n:
        if ch != '+':
            return False
    return True

def flip(n,i,K):
    num = copy.copy(n)
    for j in range(K):
        num[j+i] = '+' if num[j+i] == '-' else '-'

    return num

def flipper(x,K):
    x,cnt = list(x),0

    for i in range(len(x)-K+1):
        #print x
        if x[i] == '-':
            x = flip(x,i,K)
            cnt += 1

    if check_plus(x):
        return cnt
    return 'IMPOSSIBLE'


ans = []
test = []
for i,case in enumerate(cases):
    test.append(case[0])
    #print case
    res = flipper(case[0],int(case[1]))
    ans.append('Case #'+str(i+1)+': '+str(res))


with open('A-large.out','w') as outfile:
    for row in ans:
        outfile.write(row+'\n')

with open('infile4.txt','w') as outfile:
    for row,roww in zip(test,ans):
        outfile.write(row+' '+roww+'\n')
