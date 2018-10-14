import math

input_file = "C-small-2-attempt0.in"
output_file = "result.out"

with open(input_file) as in_file, open(output_file, 'w') as out_file:
    testcases = int(in_file.readline())
    for i in range(1, testcases + 1):
        help = in_file.readline().split()

        N = int(help[0])
        K = int(help[1])

        if K != 1:
            h = math.ceil(math.log2(K + 1))
            other = 2 ** (h - 1) - 1
            l = K - other
            prev_other = 2 ** (h - 2) - 1
            prev_other = other - prev_other

            cur = other - 1 if l <= prev_other else other
            if l > prev_other: l -= prev_other
            help_cur = 1
            l -= 1
            possible_leaf = 2 ** h - 2 ** (h - 1)
            while l != 0:
                if l % 2 == 0:
                    l = l / 2
                else:
                    help_cur += possible_leaf / 2
                    l -= 1
                    l = l / 2
                possible_leaf = possible_leaf / 2
            cur += help_cur
        else:
            cur = 0

        pos = []
        # left = true, right = false
        while cur > 0:
            parent = math.floor((cur - 1) / 2)
            pos.append(2 * parent + 1 == cur)
            cur = parent

        for p in reversed(pos):
            if N % 2 == 0:
                N = N / 2 if p else (N / 2) - 1  # left child moves to the bigger space
            else:
                N = (N - 1) / 2

        if N == 0:
            ls = 0
            rs = 0
        elif N % 2 == 0:
            ls = (N / 2) - 1
            rs = N / 2
        else:
            ls = (N - 1) / 2
            rs = (N - 1) / 2

        out_file.write('Case #{}: {} {}\n'.format(i, int(max(ls, rs)), int(min(ls, rs))))


