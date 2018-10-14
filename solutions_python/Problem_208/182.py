#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# vi: set fileencoding=utf-8 :


def solve(N, Q, E, S, D, U, V):
    position = [0 for i in range(N)]
    for i in range(N - 1):
        position[i + 1] = position[i] + D[i][i + 1]
    arrival_time = [[] for i in range(N)]
    arrival_time[0] = [0]
    for city in range(N - 1):
        minimum_arrival_time = min(arrival_time[city])
        for east_city in range(city + 1, N):
            distance = position[east_city] - position[city]
            if distance > E[city]:
                break
            arrival_time[east_city].append(minimum_arrival_time + float(distance) / S[city])
    return min(arrival_time[-1])


def answer(input_file_name):
    input_file = open(input_file_name)
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        N, Q = map(int, input_file.readline().split())
        E = []
        S = []
        for n in range(N):
            e, s = map(int, input_file.readline().split())
            E.append(e)
            S.append(s)
        D = []
        for n in range(N):
            d = list(map(int, input_file.readline().split()))
            D.append(d)
        U = []
        V = []
        for q in range(Q):
            u, v = map(int, input_file.readline().split())
            U.append(u)
            V.append(v)
        print('Case #%d: %.6f' % (case_number, solve(N, Q, E, S, D, U, V)))
    return


if __name__=='__main__':
    import sys
    answer(sys.argv[1])
