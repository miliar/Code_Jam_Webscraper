import numpy as np


def last_tidy(n):
    last_inc = 0
    for i in range(1, len(n)):
        if n[i] > n[i-1]:
            # All nice and tidy
            last_inc = i
        elif n[i] < n[i-1]:
            # OMG OMG OMG
            n[last_inc] -= 1
            n[last_inc+1:] = 9
            break
    return int(''.join([str(d) for d in n]))



if __name__=='__main__':
    # PATH_IN = 'B-small-attempt0.in'
    PATH_IN = 'B-large.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = next(f_in)
    for i, line in enumerate(f_in):
        print(line.strip())
        n = np.array([int(c) for c in line.strip()])
        res = last_tidy(n)

        print('Case #%i: %s' % (i+1, res))
        print()
        f_out.write('Case #%i: %s\n' % (i+1, res))
