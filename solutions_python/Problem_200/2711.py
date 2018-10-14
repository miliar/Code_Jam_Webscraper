import os

input_file = 'B-small.in'
out_file = input_file.replace('.in', '.out')
data = os.path.join(os.path.dirname(__file__), input_file)
data_o = os.path.join(os.path.dirname(__file__), out_file)

d2n = {1: 9, 2: 8, 3: 7, 4: 6, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1}


def get_pos(n):
    # one-digits
    m = 9
    if n <= m:
        return n
    # two-digits
    for f_d in range(1, 10):
        m += 10 - f_d
        if n <= m:
            return f_d * 10 + (9 - (m - n))
    # three-digits
    for f_d in range(1, 10):
        for s_d in range(f_d, 10):
            m += 10 - s_d
            if n <= m:
                return f_d * 100 + s_d * 10 + (9 - (m - n))
    # four-digits
    for f_d in range(1, 10):
        for s_d in range(f_d, 10):
            for t_d in range(s_d, 10):
                m += 10 - t_d
                if n <= m:
                    return f_d * 1000 + s_d * 100 + t_d * 10 + (9 - (m - n))
    # five-digits
    for z_d in range(1, 10):
        for f_d in range(z_d, 10):
            for s_d in range(f_d, 10):
                for t_d in range(s_d, 10):
                    m += 10 - t_d
                    if n <= m:
                        return z_d * 10000 + f_d * 1000 + s_d * 100 + t_d * 10 + (9 - (m - n))


def get_tidy(n):
    digits = [int(it) for it in str(n)]
    problem = None
    l = len(digits)
    for i in range(l - 1):
        if digits[i] > digits[i + 1]:
            while digits[i] == 0 or i > 0 and digits[i] - 1 < digits[i - 1]:
                i -= 1
            problem = i
            break
    if problem is None:
        return n

    d = digits[problem]
    return int(''.join(str(it) for it in digits[: problem] + [d - 1] + [9] * (l - problem - 1)))


with open(data, 'r') as f:
    with open(data_o, 'w+') as ff:
        T = int(f.readline().strip('\n'))
        for i in range(1, T + 1):
            n = int(f.readline().strip('\n'))
            ff.write('Case #%i: %s\n' % (i, get_tidy(n)))
