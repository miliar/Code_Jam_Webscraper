import sys, math
from multiprocessing import Pool


def main(data):
    N, schedule = data
    WP = [0 for i in range(N)]
    OWP = [0 for i in range(N)]
    OOWP = [0 for i in range(N)]
    
    owp = [[None for j in range(N)] for i in range(N)]
    for i in range(N):
        w = 0
        t = 0
        for j in range(N):
            r = schedule[i][j]
            if r == '1':
                w += 1
                t += 1
            elif r == "0":
                t += 1
        WP[i] = float(w) / float(t)
        for j in range(N):
            if i == j:
                continue
            r = schedule[i][j]
            if r == '1':
                owp[i][j] = (float(w) - 1.0) / (float(t) - 1.0)
            elif r == "0":
                owp[i][j] = (float(w)) / (float(t) - 1.0)
    owp = zip(*owp)
    for i in range(N):
        a = 0
        b = 0.0
        for j in range(N):
            if owp[i][j] is not None:
                b += owp[i][j]
                a += 1
        OWP[i] = b / float(a)
    for i in range(N):
        a = 0
        b = 0.0
        for j in range(N):
            r = schedule[i][j]
            if r != ".":
                a += 1
                b += OWP[j]
        OOWP[i] = b / float(a)
    
    result = [0 for i in range(N)]
    for i in range(N):
        result[i] = 0.25 * WP[i] + 0.5 * OWP[i] + 0.25 * OOWP[i]
    return "\n" + "\n".join(map(lambda x: str(x), result))
        
        

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = open("test.txt")
    T = int(f.readline())
    data = []
    for i in range(T):
        N = int(f.readline())
        s = list()
        for j in range(N):
            s.append(list(f.readline().strip()))

        data.append((N, s))
    
    pool = Pool()
    r = pool.map(main, data)
#    r = map(main, data)
    for i in range(T):
        print "Case #%d: %s" % (i+1, r[i]) 