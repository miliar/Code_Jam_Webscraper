def solve(C, F, X):
    # time to get i-th Factory.
    F_time = [0]
    # number of seconds it takes when I don't have any Factories.
    min_sec = X / 2.0

    if C >= X:
        return min_sec

    num_of_factory = 0
    # for num_of_factory in range(1, (int(F_max) + 1) + 100):
    while 1:
        num_of_factory += 1
        own_factory = num_of_factory - 1
        gain_cookie = (2.0 + (own_factory * F))
        F_time.append(F_time[num_of_factory - 1] + (C / gain_cookie))
        if F_time[num_of_factory] > min_sec:
            break

        own_factory += 1
        gain_cookie += F

        sec = F_time[num_of_factory] + (X / gain_cookie)
        if sec < min_sec:
            min_sec = sec

    return min_sec


f_in = open('B-large.in', 'r')
f_out = open('B-large.out', 'w')

# f_in = open('sample.in', 'r')
# f_out = open('sample.out', 'w')

is_first = True
p_cnt = 1

for line in f_in:
    if is_first:
        T = int(line)
        is_first = False
    else:
        inputs = line.split()
        C = float(inputs[0])
        F = float(inputs[1])
        X = float(inputs[2])
        ans = solve(C, F, X)
        if p_cnt != T:
            f_out.write('Case #%d: %.7f\n' % (p_cnt, ans))
            p_cnt += 1
        else:
            f_out.write('Case #%d: %.7f' % (p_cnt, ans))
