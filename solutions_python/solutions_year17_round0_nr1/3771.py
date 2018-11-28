# Test Pancake
#S 스트링과 K 값을 받는다. 
#S 스트링을 S-list로 변환한다. 
#S-list 값을 S-list[0]부터 읽는다. S-list[len(S)-1]까지 읽는다. 
#S-list[n]값이 ‘+’값이면 계속 진행한다. -> S-list[n+1]값을 읽는다. 
#S-list[n]값이 ‘-‘ 값이면 S-list[n]값을 ‘+’로 바꾼다. count를 1올린다.  S-list[n+1]값이 ‘+’이면 ‘-‘으로 바꾼다, S= list
#S-list[n-k]값까지 같은 과정을 진행한다.
#S-list[n-k]부터 S-list[n-1]까지 ‘-‘값이 없으면 count를 return하고, ‘-‘값이 있으면 ‘impossible’을 return한다. 

def flip(pancake):
    if pancake == '+':
        pancake = '-'
    elif pancake == '-':
        pancake = '+'
    return pancake


def solve(S):
    count = 0 
    len_str = len(S)     
 
    if len_str == K:
        if S[0] == '-':
            count +=1
            for j in range(0, len_str):
                S[j] = flip(S[j])
    else:
        for i in range(0, len_str-K+1):
            if S[i] == '-':
                count += 1
                for j in range(i, i+K):
                    S[j] = flip(S[j])
     
    for i in range(len_str-K+1, len_str):
        if S[i] == '-':
            return 'IMPOSSIBLE'
    
    return count

T = int(input())

for case_number in range(1, T+1):
    A, N = input().split()
    K = int(N)
    S = list(A)
    print('Case #%d:' % case_number, solve(S))

    
