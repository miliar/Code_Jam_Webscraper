# https://code.google.com/codejam/contest/8294486/dashboard

if __name__ == "__main__":
    filein = open('20171BA.in', 'r')
    fileout = open('20171BA.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        fileout.write('Case #%d: ' % (t + 1))
        [D, N] = map(int, filein.readline().split())
        KS = []
        for i in range(N):
            KS.append(tuple(map(int, filein.readline().split())))
        KS.sort(key=lambda ks: ks[1]) # low speed first
        KS.sort(key=lambda ks: -ks[0])
        prev_time = 0
        prev_dist = D
        prev_speed = float('inf')
        for i in range(N):
            k, s = KS[i]
            time = max((D - k) / s, prev_time)
            prev_time, prev_dist = time, k
        speed = D / prev_time
        fileout.write(str(speed) + '\n')

    filein.close()
    fileout.close()
