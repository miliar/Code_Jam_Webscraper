import fileinput
# from time import time

def solve(S, K):
    # start = time()
    n_pancakes = len(S)
    if n_pancakes < K:
        return 'IMPOSSIBLE'

    d = {}
    def helper(cur, n_flips):
        tmp = tuple(cur)
        if tmp in d:
            if d[tmp] <= n_flips:
                return float('inf')
            else:
                d[tmp] = n_flips
        else:
            d[tmp] = n_flips

        if sum(cur) == n_pancakes:
            return n_flips

        res = []
        for i in range(n_pancakes - K + 1):
            # flip
            for j in range(K):
                cur[i + j] *= -1
            res.append(helper(cur, n_flips + 1))
            # flip back
            for j in range(K):
                cur[i + j] *= -1

        return min(res)

    res = helper(S, 0)

    # end = time()
    # print(end-start)
    # for key in d:
    #     print(key, d[key])


    if res == float('inf'):
        return 'IMPOSSIBLE'
    else:
        return res


def reformat(S):
    f = lambda s: 1 if s == '+' else -1
    return list(map(f, S))

if __name__ == '__main__':
    f = fileinput.input()
    T = int(f.readline())
    for i in range(T):
        S, K = f.readline().split()
        K = int(K)
        res = solve(reformat(S), K)
        print("Case #{}: {}".format(i + 1, res))
