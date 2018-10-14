a = int(input())
for i in range(a):
    b = input().split()
    K = int(b[-1])
    S = b[0]
    checker = '-'+'+'*(K-1)+'-'
    c = 0
    while True:
        if (S.count('-')==0):
            print('Case #'+str(i+1)+': '+str(c))
            break
        elif ((S.count(checker)<=0) and (S.count('-')<K)):
            print('Case #'+str(i+1)+': '+'IMPOSSIBLE')
            break
        else:
            index = S.index('-')
            S = list(S)
            for j in range(index,index+K):
                if S[j]=='+':
                    S[j] = '-'
                else:
                    S[j] = '+'
            c+=1
            S=''.join(S)
