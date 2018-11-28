import sys

name = "C-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

T = int(input())

for testCase in range(T):
    N, K = (int(x) for x in input().split())
    ans = N
    depth = K.bit_length()
    p = 1 << depth
    ans //= p

    layer_size = p
    big_count = (N % layer_size) + 1

    pair_num = K - (layer_size // 2) + 1

    big_pairs = big_count - (layer_size // 2)

    if big_pairs == 0:
        res = (ans, ans-1)

    if big_pairs > 0:
        if big_pairs - pair_num >= 0:
            res = (ans, ans)
        else:
            res = (ans, ans-1)

    if big_pairs < 0:
        if (layer_size // 2) + big_pairs - pair_num >= 0:
            res = (ans, ans-1)
        else:
            res = (ans-1, ans-1)


    print("Case #" + str(testCase + 1) + ": " + ("%d %d" % res))