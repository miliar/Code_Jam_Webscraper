from collections import defaultdict

def solve(test_num):
    n, k = map(int, input().strip().split())

    cnts = {n: 1}
    while k > 0:
        new_cnts = defaultdict(int)
        for size, cnt in sorted(cnts.items(), reverse=True):
            if k - cnt > 0:
                k -= cnt
            else:
                left = size // 2
                right = size // 2
                if size % 2 == 0:
                    left -= 1

                print("Case #{}: {} {}".format(test_num, right, left))
                return

            if size % 2 == 0:
                new_cnts[size//2 - 1] += cnt
                new_cnts[size//2] += cnt
            else:
                new_cnts[size//2] += cnt
                new_cnts[size//2] += cnt

        cnts = new_cnts


T = int(input())

for i in range(T):
    solve(i + 1)
