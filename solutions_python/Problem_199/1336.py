import multiprocessing as mp
import sys

def solve(S, K):
    INF = 2**32
    HAPPY = '+'
    BLANK = '-'
    GOOD = ''.join([HAPPY for _ in S])
    def flip(s, start, end):
        s = list(s)
        for i in range(start, end):
            if s[i] == HAPPY:
                s[i] = BLANK
            elif s[i] == BLANK:
                s[i] = HAPPY
        return ''.join(s)
    def brute_force(S, K):
        sys.setrecursionlimit(5000)
        def dfs(s, flips, last_states):
            if s == S:
                return flips
            if s in last_states and last_states[s] <= flips:
                return INF
            last_states[s] = flips
            flips += 1
            return min(dfs(flip(s, i, i+K), flips, last_states) for i in range(len(S)-K+1))
        last_states = {} # s:flips
        return dfs(GOOD, 0, last_states)
    def greedy(S, K):
        flips = 0
        while S != GOOD:
            for i in range(len(S)-K+1):
                if S[i] == BLANK:
                    flips += 1
                    S = flip(S, i, i+K)
                    break
            else:
                if S != GOOD:
                    return INF
        return flips
    #ret = brute_force(S, K)
    ret = min(greedy(S, K), greedy(S[:], K))
    if ret != INF:
        return ret
    else:
        return 'IMPOSSIBLE'

if __name__ == '__main__':
    pool = mp.Pool(mp.cpu_count())
    case_num = int(raw_input())
    results = []
    for i in range(1, case_num+1):
        s, k = raw_input().split()
        results.append(pool.apply_async(solve, args=(str(s), int(k))))
    output = [p.get() for p in results]
    pool.close()
    pool.join()
    for i,out in enumerate(output):
        print 'Case #%d: %s' % (i+1, str(out))
