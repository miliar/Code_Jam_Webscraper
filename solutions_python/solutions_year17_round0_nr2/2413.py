f_in = open('B-large.in')
f_out = open('B-large.out', 'w')

T = int(f_in.readline())

def solve():
    N = f_in.readline().rstrip()

    # special case; single digit
    if len(N) == 1:
        return N

    for i in range(1, len(N)):
        prev = int(N[i-1])
        curr = int(N[i])
        if curr >= prev:
            continue
        # hit first decrement.
        # special case: 0 prefixed by 1 -> return all 9s
        if curr == 0 and prev == 1:
            return '9' * (len(N) - 1)
        # otherwise: decrement first instance of prev and then put all 9s after
        first_prev_i = N.find(str(prev))
        return N[:first_prev_i] + str(prev - 1) + '9' * (len(N) - first_prev_i - 1)

    # if we got here the whole thing is already OK
    return N

for case in range(1, T + 1):
    f_out.write('Case #{}: {}\n'.format(case, solve()))

f_in.close()
f_out.close()
