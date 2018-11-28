#!/usr/bin/python

def main():
    T = int(raw_input())
    for t in range(1, T + 1):
        inp = raw_input().split()
        N = int(inp[0])
        S = int(inp[1])
        p = int(inp[2])
        assert(S<=N)
        assert(p>=0 and p<=10)
        if p > 0:
            min_non_surprising_sum = p + 2 * (p-1)
        else:
            min_non_surprising_sum = 0
        if p >= 2:
            min_surprising_sum = p + 2*(p - 2)
        else:
            min_surprising_sum = 50
        count = 0
        for i in range(3, N + 3):
            s = int(inp[i])
            if s >= min_non_surprising_sum:
                count += 1
            elif S > 0 and s >= min_surprising_sum:
                count += 1
                S -= 1
        print "Case #" + str(t) + ": " + str(count)

if __name__ == '__main__':
    main()
