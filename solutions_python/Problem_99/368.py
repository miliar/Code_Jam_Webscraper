import time, itertools

def Solve(data):
    print data
    A = data[0][0]
    B = data[0][1]
    p = data[1]
    pr = []
    pr.append(2 + B)
    for backs in range(0, A+1):
        correct = 1
        for test in p[:A-backs]:
            correct = correct * test
        exp = correct * (B - A + 1 + 2*backs) + (1-correct) * ((B-A+1) + B + 1 + 2*backs)
        print "backs",backs, "correct",correct,"exp", exp
        pr.append(exp)

    #print data
    return sorted(pr)[0]


if __name__ == '__main__':
    from multiprocessing import Pool  
    start = time.time()

    fin = open('a.in')
    fout = open('a.out','w')
    T = int(fin.readline())
    data = []
    for t in range(T):
        d = []
        d.append(map(int, fin.readline().split()))
        d.append(map(float, fin.readline().split()))
        data.append(d)

    pool = Pool()  
    results = pool.map(Solve, data)

    c = 0
    for result in results:
        c = c + 1
        fout.write("Case #%d: %.6f\n" % (c, result))
        print result

    elapsed = (time.time() - start)
    print elapsed