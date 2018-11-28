def solve(M, N, S):
    """ solve the problem """

    #print(M, N, S)

    all_servers = [[[] for _ in range(N)]]
    for s in S:
        next_all_servers = []
        for servers in all_servers:
            for i in range(N):
                _servers = [s[:] for s in servers]
                _servers[i].append(s)
                next_all_servers.append(_servers)
        all_servers = next_all_servers


    #N = 1
    #if N == 2:
    def compute(_S):
        container = set()
        for s in _S:
            for i in range(len(s)+1):
                container.add(s[:i])
        count = len( container )
        return count

    result = {}
    for servers in all_servers:
        count = 0
        for server in servers:
            count += compute(server)

        result[count] = result.get(count, 0) + 1

    k = max(result.keys())
    v = result[k]

    return '%d %d' % (k, v)


def parse():
    """ parse input """

    M, N = map(int, input().split(' '))
    S = []
    for i in range(M):
        S.append(input())

    return M, N, S


def main():
    
    T = int(input())

    # solve
    for t in range(1, T+1):
        params = parse()
        result = solve(*params)
        print('Case #%d: %s' % (t, result))


if __name__ == '__main__':

    main()
