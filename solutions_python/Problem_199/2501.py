def minFlip(S, K):
    K = int(K)
    flipArray = [0] * len(S)
    flips = 0
    # fix the tail part first
    for i in range(1, K):
        if (i + K) <= len(S):
            if ( (flipArray[-i] % 2) and (S[-i] == '+') ) or \
            ( (not (flipArray[-i] % 2) ) and (S[-i] == '-') ):
                flips += 1
                for j in range(K):
                    flipArray[-i-j] += 1
    # flip the head part
    for i in range( len(S)-K + 1):
        if ( (flipArray[i] % 2) and (S[i] == '+') ) or \
         ( (not (flipArray[i] % 2) ) and (S[i] == '-') ):
            flips += 1
            for j in range(K):
                flipArray[i+j] += 1
    for i in range(1, K+1):
        if ( (flipArray[-i] % 2) and (S[-i] == '+') ) or \
            ( (not (flipArray[-i] % 2) ) and (S[-i] == '-') ):
            return "IMPOSSIBLE"
    return flips

sample = int(input())
for case in range(1, sample+1):
    S, K = input().split(" ")
    print("Case #{}: {}".format(case, minFlip(S, K) ) )