import numpy as np

def main():
    T = int(input())
    for i in range(T):
        N, K = [int(a) for a in input().split()]
        exp = np.floor(np.log2(K))
        small = int(np.floor((N-2**exp+1)/2**exp))
        big = small+1
        NumBig = (N-2**exp+1)-small*(2**exp)
        NumSmall = 2**exp-NumBig
        rest = NumBig - K + 2**exp - 1
        if rest >= 0:
            print('Case #{}: {} {}'.format(i+1, int((big)/2), int((big-1)/2)))
        else:
            print('Case #{}: {} {}'.format(i+1, int((small)/2), int((small-1)/2)))


if __name__ == '__main__':
    main()
