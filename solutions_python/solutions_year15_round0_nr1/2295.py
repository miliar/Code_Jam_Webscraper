import numpy as np

f_in = open('standing_ovation.in', 'r')
f_out = open('standing_ovation.out', 'w')

def solve (case, N, people):
    total = 0
    N = int(N)
    num_shy = np.array([int(people[i]) for i in range(N + 1)])
    cum_sum = np.cumsum(num_shy)
    needed = np.array([i+1 for i in range(N + 1)])
    print case
    print num_shy
    print cum_sum
    print needed

    for i in range(1, N+1):
        if num_shy[i]:
            new_ppl = needed[i-1] - cum_sum[i-1]
            if new_ppl > 0:
                num_shy[i] += new_ppl
                cum_sum = np.cumsum(num_shy)
                total += new_ppl
    print total
    f_out.write('Case #' + str(case) + ': ' + str(total) + "\n")
    return total


T = f_in.readline()
case = 0
for line in f_in:
    case += 1
    N, people = line.split()
    solve(case, N, people)
