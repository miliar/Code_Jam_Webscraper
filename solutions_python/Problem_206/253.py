#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
# vi: set fileencoding=utf-8 :


def solve(D, N, K, S):
    maximum_time = 0
    for i in range(N):
        maximum_time = max(maximum_time, float(D - K[i]) / S[i])
    return D / maximum_time 


def answer(input_file_name):
    input_file = open(input_file_name)
    T = int(input_file.readline())
    for case_number in range(1, T + 1):
        D, N = map(int, input_file.readline().split())
        cake = []
        K = []
        S = []
        for n in range(N):
            k, s = map(int, input_file.readline().split())
            K.append(k)
            S.append(s)
        print('Case #%d: %.6f' % (case_number, solve(D, N, K, S)))
    return


if __name__=='__main__':
    import sys
    answer(sys.argv[1])
