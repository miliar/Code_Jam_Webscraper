import multiprocessing as mp

def solve(N):
    def is_good(n):
        for i in range(len(n)-1):
            if n[i] > n[i+1]:
                return False
        return True
    def brute_force(N):
        n = int(N)
        for i in xrange(n, 0, -1):
            if is_good(str(i)):
                return i
    def greedy(N):
        while True:
            for i in range(len(N)-1):
                if N[i] > N[i+1]:
                    N = str(int(N[:i+1] + ''.join(['0' for _ in N[i+1:]]))-1)
                    break
            else:
                return N
    return greedy(N)

if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())
    case_num = int(raw_input())
    results = []
    for i in range(1, case_num+1):
        N = str(raw_input())
        results.append(pool.apply_async(solve, args=(N,)))
    output = [p.get() for p in results]
    pool.close()
    pool.join()
    for i,out in enumerate(output):
        print 'Case #%d: %s' % (i+1, str(out))
