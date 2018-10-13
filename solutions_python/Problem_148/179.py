from collections import deque

if __name__ == '__main__':
    T = input()
    with open('A-big.output.txt', 'w') as f:
        for t in xrange(1, T + 1):
            N, X = map(int, raw_input().split())
            S = map(int, raw_input().split())
            S.sort(reverse=True)
            S = deque(S)
            ret = 0
            while S:
                if len(S) == 1:
                    S.pop()
                    ret += 1
                elif S[0] + S[-1] <= X:
                    S.popleft()
                    S.pop()
                    ret += 1
                else:
                    S.popleft()
                    ret += 1
            f.write("Case #%d: %d\n" % (t, ret))