__author__ = 'Shailesh'

with open("../files/B-small-attempt0.in", 'r') as inp, open("../files/outputB.txt", 'w') as out:
    t = int(inp.readline())
    for i in xrange(t):
        string = "Case #" + str(i+1) + ": "
        A, B, K = map(int, inp.readline().split())
        if B < A:
            A, B = B, A
        if A <= K:
            answer = A * B
            out.write(string + str(answer) + "\n")
            continue

        answer = B * K

        b = B - 1
        k = K - 1
        size = len(bin(b)) - 2
        for i in xrange(K, A):
            for j in xrange(B):
                if i & j < K:
                    # print i * j
                    answer += 1

        out.write(string + str(answer) + "\n")