import numpy as np

def cruise_controll(D, N, positions, speeds):
    positions = np.array(positions)
    speeds = np.array(speeds)

    arrival_time = (D - positions) / speeds
    my_arrival_time = arrival_time.max()

    return D / my_arrival_time



if __name__=='__main__':
    PATH_IN = 'A-large.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = int(f_in.readline())
    for t in range(T):
        line = f_in.readline()
        print(line.strip())

        D, N = line.split()
        D = int(D)
        N = int(N)
        positions = []
        speeds = []
        for _ in range(N):
            line = f_in.readline()
            k, s = line.split()
            positions += [int(k)]
            speeds += [int(s)]

        res = '%.6f' % cruise_controll(D, N, positions, speeds)

        print('Case #%i: %s' % (t+1, res))
        print()
        f_out.write('Case #%i: %s\n' % (t+1, res))