
def S2list(S):
    ss = []
    for i in range(len(S)):
        if S[i] == '+':
            ss.append(1)
        else: # '-'
            ss.append(0)
    return ss

def OversizedPancakeFlipper(ss, K):
    # print(ss)
    l = len(ss)
    if K > l:
        sss = [i % 2 for i in ss]
        if 0 in sss:
            flip = -1001 # impossible
        else:
            flip = 0
    else:
        flip = 1
        flag = -1
        
        for i in range(K):
            ss[i] += 1
            if ss[i] % 2 == 0 and flag == -1:
                flag = i

        if flag > 0:
            flip += OversizedPancakeFlipper(ss[flag:], K)
        else:
            sss = [i % 2 for i in ss[K:]]
            for i in range(l - K):
                if sss[i] == 0:
                    break
            if K + i < l:
                flip += OversizedPancakeFlipper(ss[K + i:], K)

    return flip
    

# def main():
T = int(input())

for i in range(T):
    sk = input()
    SK = [n for n in sk.split()]
    try:
        st = SK[0].index('-')
    except ValueError:
        print("Case #%d: "%(i + 1), end='')
        print(0)
        continue
    
    ss = S2list(SK[0])
    K = int(SK[1])

    # print(SK)

    print("Case #%d: "%(i + 1), end='')
    flip = OversizedPancakeFlipper(ss[st:], K)
    if flip < 0:
        print('IMPOSSIBLE')
    else:
        print(flip)
    
