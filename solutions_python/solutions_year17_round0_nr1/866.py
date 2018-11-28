import sys

def solve(config, K):
    n = 0
    config = list(x == '+' for x in config)

    for i in range(len(config)-K+1):
        if not config[i]:
            n += 1
            for j in range(i,i+K):
                config[j] = not config[j]

    if all(config):
        return str(n)
    else:
        return "IMPOSSIBLE"


if __name__ == "__main__":
    sys.stdin = open('A-large.in')
    sys.stdout = open('out.txt', 'w')

    N = int(raw_input())


    for n in range(N):
        config, K = raw_input().split(" ")

        print "Case #%d: %s" % (n + 1, solve(config, int(K)))
