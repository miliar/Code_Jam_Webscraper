def ascend(N):
    for i in range(len(N)-1):
        if int(N[i]) > int(N[i+1]):
            return False
    return True

def to_num(N):
    while N[0] == '0':
        del N[0]
    n = ''
    for i in N:
        n += i
    return int(n)

def compute(N):
    i = 0
    while not ascend(N):
        a = int(N[i])
        b = int(N[i+1])
        if a > b:
            i = N.index(str(a))
            N[i] = str(a-1)
            for j in range(i+1, len(N)):
                N[j] = '9'
        i += 1
    return to_num(N)

file = open('tidy_big.txt')
ANS = open('tidy_big_ans.txt','w')

T = int(file.readline())
for i in range(T):
    N = list(str(int(file.readline())))
    ans = compute(N)
    a = str('Case #%d: %d\n'%(i+1,ans))
    ANS.write(a)

"""
T = int(input())

for i in range(T):
    N = list(input())
    print(ANS(N))
"""
