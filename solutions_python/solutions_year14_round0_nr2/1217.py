import fileinput
from math import ceil

optimal_N = lambda C,F,X,N: C*sum([1./(2+i*F) for i in range(N)]) + X/(2+N*F)
optimal_time = lambda C,F,X:  optimal_N(C,F,X,max(int(ceil(X/C-1-2/F)),0))

def main():
    fin = fileinput.input()
    T = int(next(fin)) # number of test cases
    for case in range(1, T+1):
        C,F,X = [float(x) for x in next(fin).split(" ")]
        print("Case #{}: {}".format(case, optimal_time(C,F,X)))
    fin.close()

if __name__ == '__main__':
    main()
