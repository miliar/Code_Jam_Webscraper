from math import log
'''
Bathroom Stalls
'''


def main():
    t = int(input())
    for x in range(1, t + 1):
        y, z = (0, 0)
        N, K = (int(n) for n in input().split())
        base = int(log(K, 2))
        ix = K - 2 ** base
        stalls = [N]
        for i in range(base):
            new_stalls = []
            for s in stalls:
                new_stalls += [(s - 1) // 2, (s - 1) // 2 + (s - 1) % 2]
            stalls = new_stalls
        stalls.sort(reverse=True)
        N = stalls[ix]
        # print(stalls)
        # print(len(stalls))
        # print(ix)
        y, z = ((N - 1) // 2 + (N - 1) % 2, (N - 1) // 2)
        print ("Case #{}: {} {}".format(x, y, z))


if __name__ == '__main__':
    main()
