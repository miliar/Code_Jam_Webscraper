from math import log, floor, ceil

def calculate_distances(N):
    """
    Given an integer N, calculates the smallest and the largest distance between the middle and an extreme
    :param N: 
    :return: d and D,  the smallest and largest distance
    """
    return floor((N-1)/2), ceil((N-1)/2)


with open("./C-small-2-attempt1.in", "r") as fin:
    with open("./C-small-2-attempt1.out", "w+") as fout:
        T = int(fin.readline().strip("\n"))
        print(T)
        for i in range(T):
            print (i)
            N, K = fin.readline().strip("\n").split()
            N = int(N)
            K = int(K)
            m = 0
            M = 0
            tier = int(log(K, 2))
            # This recreates the path choosing the correct interval at every ramification
            for t in range(tier+1):
                m, M = calculate_distances(N)
                N = M if K % 2 == 0 else m
                K = K//2
            fout.write("Case #%d: %d %d\n" % (i + 1, M, m))