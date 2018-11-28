import math
f = open('B-small-practice.in', 'r')
T = int(f.readline())
def tidy_num(i):
    num = [int(x) for x in f.readline().strip()]
    K = len(num) - 1
    while(K >= 0):
        temp = K - 1
        minv = math.inf
        while(temp > -1 and num[temp] <= num[K]):
            minv = min(minv, num[temp])
            if minv < num[temp]:
                break
            temp -= 1
        if temp > -1:
            num[temp] -= 1
            while temp+1 <= K:
                num[temp+1] = 9
                temp += 1
        else:
            break
        K -= 1
    print ('Case #%d: %d' % (i+1, int("".join([str(x) for x in num]))))




for i in range(T):
    tidy_num(i)
    # if result == -1:
    #     print ('Case #%d: %s' % (i+1, "IMPOSSIBLE"))
    # else:
    #     print ('Case #%d: %d' % (i+1, result))
    # print >>stderr, 'Case #%d: %d' % (T, N-best)





