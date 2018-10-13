# coding: utf8
# Copyright: MathDecision


def minvel(k, s, d):
    return s * d / (d - k)

def sol(horses, d):
    k, s = min(horses, key=lambda x: minvel(x[0], x[1], d))
    return minvel(k, s, d)


if __name__ == '__main__':
    file_number = 2
    problem_name = 'cruisecontrol'
    infile = '{}{}.in'.format(problem_name, file_number)
    outfile = '{}{}.out'.format(problem_name, file_number)
    responses = []
    with open(infile, 'r') as f:
        cases = int(f.readline())
        for _ in range(cases):
            D, N = map(lambda x: int(x), f.readline().split(' '))
            horses = []
            for i in range(N):
                K, S = map(lambda x: float(x), f.readline().split(' '))
                horses.append((K, S))
            # print D, N, horses
            # print sol(horses, D)
            responses.append(sol(horses, D))

    with open(outfile, 'w') as f:
        for i, r in enumerate(responses):
            f.write('Case #{}: {}\n'.format(i + 1, r))
