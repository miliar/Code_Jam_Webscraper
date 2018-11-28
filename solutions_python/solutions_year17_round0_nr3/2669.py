
def solve(N, K):
    oc_list = [N]

    def process(k, o_list):
        o_list = sorted(o_list)
        n = o_list.pop()

        if n == 1:
            return 0, 0
        if k == 1:
            return int(n/2), int(n/2)-1 if n % 2 == 0 else int(n/2)

        if n % 2 == 0:
            o_list.append(int(n/2))
            if n > 2:
                o_list.append(int(n/2)-1)
        else:
            if n > 1:
                o_list.append(int(n/2))
                o_list.append(int(n/2))

        return process(k-1, o_list)

    return process(K, oc_list)


t = int(input())
for i in range(1, t + 1):
    N, K = (s for s in input().split(" "))
    max_s, min_s = solve(int(N), int(K), )
    print("Case #{}: {} {}".format(i, max_s, min_s))

