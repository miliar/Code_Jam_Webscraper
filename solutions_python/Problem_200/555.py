import numpy as np


def main():
    T = int(input())
    for tid in range(T):
        N = input()
        pivot = -1
        chkpnt = 0
        for i in range(len(N) - 1):
            if N[i] > N[i + 1]:
                pivot = chkpnt
                break
            elif N[i] < N[i + 1]:
                chkpnt = i + 1
        if pivot == -1:
            print("Case #{}: {}".format(tid + 1, N))
        else:
            print("Case #{}: {}".format(tid + 1, int(N[:pivot] + chr(ord(N[pivot]) - 1) + "9" * (len(N) - pivot - 1))))



if __name__ == '__main__':
    main()