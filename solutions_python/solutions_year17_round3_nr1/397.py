import math

def solve(cakes, n, k):
    copies = []
    for i in range(len(cakes)):
        if cakes[i][0] > cakes[n][0] or i == n:
            continue
        copies.append(2*cakes[i][0]*math.pi*cakes[i][1])
    copies = sorted(copies, reverse=True)
    #print(copies)
    res = cakes[n][0]*math.pi*2*cakes[n][1]
    #print("default:%f"%(res))
    if len(copies) < k-1:
        return -1
    for i in range(k-1):
        res += copies[i]
    #print("res:%f"%(res + cakes[n][0]**2*math.pi))
    #print("round: %f"%(((cakes[n][0]**2)*math.pi)))
    return res + ((cakes[n][0]**2)*math.pi)


def main():
    fname = 'A-large.in'
    fname_out = 'A-large.out'
    fout = open(fname_out, 'wt')
    with open(fname) as fin:
        T = int(fin.readline().strip())
        for t in range(1, T+1):
            N, K = list(map(int, fin.readline().strip().split(' ')))
            cakes = []
            for i in range(N):
                cakes.append(list(map(int, fin.readline().strip().split(' '))))

            res = 0.0
            for i in range(N):
                #print(i, cakes)
                res = max(res, solve(cakes, i, K))
            print("Case #%d: %.10f" % (t, res))
            fout.write("Case #%d: %.10f\n" % (t, res))

if __name__ == '__main__':
    main()
