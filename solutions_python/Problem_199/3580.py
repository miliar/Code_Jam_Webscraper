def solve(config):
    config, k = config.split()
    k = int(k)
    config = list(config)
    ii = 0
    cnt = 0

    while ii <= len(config) - k:
        if config[ii] == '+':
            ii += 1
        else:
            for jj in range(ii, ii + k):
                if config[jj] == '-':
                    config[jj] = '+'
                else:
                    config[jj] = '-'
            cnt += 1

    if '-' in config:
        return 'IMPOSSIBLE'
    else:
        return cnt

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t + 1):
        config = input()
        result = solve(config)
        print("Case #{}: {}".format(i, result))
