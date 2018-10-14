def read_one(stream, type_to_read=int):
    return type_to_read(stream.readline().strip())


def read_several(stream, type_to_read=int):
    return [type_to_read(x) for x in stream.readline().strip().split()]


def switch(S, K, begin):
    for i in range(begin, begin + K):
        S[i] = '-' if S[i] == '+' else '+'


def solve(S, K):
    begin = 0
    n_moves = 0
    while 1:
        while begin < len(S) and S[begin] == "+":
            begin += 1
        if begin == len(S):
            return n_moves
        elif begin > len(S) - K:
            return "IMPOSSIBLE"
        else:
            n_moves += 1
            switch(S, K, begin)
    return n_moves


if __name__ == "__main__":
    import sys
    stream = sys.stdin
    T = read_one(stream, int)
    for t in range(T):
        S1 = read_several(stream, str)
        S = [x for x in S1[0]]
        K = int(S1[1])

        solution = solve(S, K)
        print("Case #{id}: {sol}".format(id=t+1, sol=solution))




