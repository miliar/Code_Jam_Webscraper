f = open('B-small-practice.in', 'r')
T = int(f.readline())
def min_flap():
    temp = f.readline().split()
    S = list(temp[0])
    K = int(temp[1])
    k, L = 0, len(S)
    counter = 0
    while(k < L):
        if S[k] == "-":
            if k + K -1 >= L:
                return -1
            else:
                counter += 1
                temp = k
                while temp < k + K :
                    S[temp] = "-" if S[temp] == "+" else "+"
                    temp += 1
        k += 1
    return counter

for i in range(T):
    result = min_flap()
    if result == -1:
        print ('Case #%d: %s' % (i+1, "IMPOSSIBLE"))
    else:
        print ('Case #%d: %d' % (i+1, result))
    # print >>stderr, 'Case #%d: %d' % (T, N-best)





