#Oversized Pancake Flipper
import numpy as np
T = int(input().strip())

toord = lambda s: np.array(list(ord(ch) for ch in s))
tochr = lambda o: ''.join( chr(x) for x in list(o) )
for i in range(T):
    s, k = input().strip().split()
    k = int(k)
    n = len(s)
    s = toord(s)
    cnt = 0
    for j in range(n-k+1):
        if s[j] == ord('-'):
            s[j:(j+k)] ^= 6 #Cycles between ascii values of 43 and 45 ('+' and '-')
            #print(tochr(s))
            cnt += 1

    if( '-' in tochr(s[-k:]) ):
        cnt = "IMPOSSIBLE"
    print("Case #{}: {}".format(i+1,cnt))


'''
Find inverse under xor addition operation for a fixed mask of k bits. The operation is commutative so there is no need
to worry about the order. In addition flipping at the same place twice is pointless since the operation cancels. Every
pattern created in this way is unique.
'''
