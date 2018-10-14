f_in = open('A-large.in')
f_out = open('A-large.out', 'w')

T = int(f_in.readline())

def solve():
    S, K = f_in.readline().rstrip().split()
    K = int(K)

    # greedy from left to right
    flips = 0
    # 1 (odd) = +, 0 (even) = -
    pancakes = [1 if p == '+' else 0 for p in S]
    # iterate over all except last K
    for i in range(0, len(S) - K):
        if pancakes[i] % 2 == 0:
            # flip K starting from here
            flips += 1
            for j in range(K):
                pancakes[i+j] += 1
    # check last K
    last = [p % 2 for p in pancakes[-K:]]
    if sum(last) == 0:
        flips += 1  # one more flip - they're all 0s
    elif any([p != 1 for p in last]):
        # impossible if they're not all 0s or not all 1s
        return 'IMPOSSIBLE'

    return flips


for case in range(1, T + 1):
    f_out.write('Case #{}: {}\n'.format(case, solve()))

f_in.close()
f_out.close()
