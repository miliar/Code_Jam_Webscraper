import math
a=int(input())
for i in range(a):
    b=input().split()
    N = int(b[0])
    K = int(b[-1])
    S = '0'+'.'*N+'0'
    sub_S = '.'*N
    for j in range(K):
        while S.count(sub_S)<=0:
            sub_S = sub_S[1:]
        mid = math.ceil(len(sub_S)/2)
        index = S.index(sub_S)-1
        index += mid
        S = list(S)
        S[index] = '0'
        S=''.join(S)
    left_c = 0
    right_c = 0
    l_mark = S[index-(left_c+1)]
    while l_mark!='0':
        left_c+=1
        l_mark = S[index-(left_c+1)]
    r_mark = S[index+(right_c+1)]
    while r_mark!='0':
        right_c+=1
        r_mark = S[index+(right_c+1)]
    print('Case #'+str(i+1)+': '+str(right_c)+' '+str(left_c))
