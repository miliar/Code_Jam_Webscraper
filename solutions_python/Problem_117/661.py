import numpy as np

def read_input(filename):
    # The structure of output_list:
    # [T, [N, M, [[N1...], [N2...], ..., [NN...]]],
    #     [N, M, [[N1...], [N2...], ..., [NN...]]], ...]
    output_list = []
    input_file = open(filename, 'r')
    # T: num_case
    num_case = int(input_file.readline().strip('\n'))
    output_list.append(num_case)
    # 
    N, M = 0, 0
    for i in range(num_case):
        N, M = list(map(int, input_file.readline().strip('\n').split()))
        output_list.append([N, M, []])
        for j in range(N):
            t_line = input_file.readline().strip('\n')
            output_list[-1][2].append(list(map(int, t_line.split())))
    input_file.close()
    return output_list

def Lawnmower(data_list, max_level):    
    T = data_list[0]
    result = []
    for t in range(1, T+1):        
        N, M = data_list[t][0], data_list[t][1]        
        A = np.empty([N, M], int)
        result.append(True)
        for n in range(N):
            for m in range(M):
                A[n, m] = data_list[t][2][n][m]
        n = 0
        while n <= N - 1:
            m = 0
            while m <= M - 1:
                target = A[n, m]
                if A[n, m] < max_level:                   
                    p = ((A[n, :] == target).all() or (A[:, m] == target).all())
                    if not p:                        
                        result[-1] = False
                        m = M
                        n = N
                m = m + 1
            n = n + 1
    return result

if __name__ == '__main__':
    MAX_LEVEL = 2
    filename = 'B-small-attempt1.in'
    input_list = read_input(filename)    
    result = Lawnmower(input_list, MAX_LEVEL)
    ans_file = open('ans.txt', 'w')
    i, n = 1, input_list[0]
    print(n)
    while i <= n:
        ans = result[i-1]
        if ans:
            ans_file.write('Case #' + str(i) + ': YES\n')
        else:
            ans_file.write('Case #' + str(i) + ': NO\n')
        i = i + 1
    ans_file.close()
