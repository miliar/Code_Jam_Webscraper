import numpy as np

def check_tidy(narr):
    if len(narr) == 1:
        return True,0
    ndiff = narr[1:] - narr[:-1]
    neg_idx = np.argmax(ndiff<0)
    if neg_idx == 0:
        if ndiff[0]>=0:
            return True,0
    return False,neg_idx
    

def solve(nlist):
    narr = np.asarray(nlist)
    tidy,idx = check_tidy(narr)
    if tidy:
        return int(''.join(map(str,narr)))
    while tidy!=True:
        narr[idx] -= 1
        for j in range(idx+1, len(narr)):
            narr[j] = 9
        tidy,idx = check_tidy(narr)
    return int(''.join(map(str,narr)))

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1,t+1):
        n = [int(ele) for ele in raw_input()]
        soln = solve(n)
        print("Case #{}: {}".format(i, soln))