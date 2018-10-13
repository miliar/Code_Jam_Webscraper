T = int(input())

def isHappy(l):
    for i in l:
        if i == '-':
            return False
    return True

def flip(c):
    if c == '+':
        return '-'
    else:
        return '+'

for t in range(1, T+1):
    S, K = input().split()

    l = list(S)
    K = int(K)
    ans_l = [0 for i in range(len(l))]
    ans = ""
    cnt = 0

    if isHappy(l):
        ans = "0"
    else:

        # 1. 맨 앞인 0부터 시작해서 적어도 한번씩 쭉 뒤집는다.
        for i in range(len(l)-K+1):
            for j in range(i, i+K):
                l[j] = flip(l[j])
        cnt = len(l)-K+1 # 모두 가능한 한 번씩 뒤집음

        # 2. 맨 앞부터 쭉 훑으면서 뒤집히지 않은 부분을 뒤집는다.
        for i in range(len(l)-K+1):
            if l[i] == '-':
                # 뒤집히지 않은 부분을 찾으면 그 이후를 뒤집는다.
                # 이 때 인덱스를 넘어가면 불가능한것.
                if i + K > len(l):
                    pass
                else:
                    for j in range(i, i+K):
                        l[j] = flip(l[j])
                    cnt -= 1

    if isHappy(l):
        ans = str(cnt)
    else:
        ans = "IMPOSSIBLE"

    print("Case #" + str(t) + ": " + ans )
