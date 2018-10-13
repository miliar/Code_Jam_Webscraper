#GJAM
#inn.in
from sys import * 

def execute():
        input_name = argv[1]
        output_name = "out.txt"
        input_file = open(input_name)
        output_file = open(output_name, 'w')

        main(input_file, output_file)

        input_file.close()
        output_file.close()

def level(K):
    return K.bit_length() - 1

def level_space(N, K):
    return N - 2**(level(K)) + 1 

def min_interval_size(N, K):
    return level_space(N, K)/2**level(K)

def num_max_intervals(N, K):
    l = level(K)
    return 2**l - (min_interval_size(N, K) + 1) * 2**l + level_space(N, K) 

def K_interval(N, K):
    l = level(K)
    pos = K - 2**l + 1
    if pos <= num_max_intervals(N, K):
        return min_interval_size(N, K) + 1
    else:
        return min_interval_size(N, K)

def final(N, K):
    n = K_interval(N, K) - 1
    m = n/2
    return n - m, m

def main(input_file, output):
        # main algorithm goes here
        T = int(next(input_file))
        for i in range(T):
            N, K = [int(x) for x in next(input_file).strip().split()]
            f = final(N, K)
            output.write("Case #%i: %i %i\n" % (i+ 1, f[0], f[1] ))

execute()
