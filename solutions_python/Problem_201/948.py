#aditya76
import sys
def main():
    neha = arrange_input()
    #file=open('output.txt','w')
    for i, N, K in neha:
        r = adi(N, K)
        r = ' '.join(str(x) for x in r)
        #file.write(f'Case #{i}: {r}\n')
        print(f'Case #{i}: {r}')

'''
arrange inputs //aditya76

'''
def arrange_input():
    T = int(input())
    for i in range(1, T + 1):
        N, K = [int(x) for x in input().split()]
        yield i, N, K

'''
solve C //aditya76

'''
def adi(N, K):
    if K == N:
        return 0, 0
    n = N - 1
    a = n // 2
    b = n - a
    k = K - 1
    ka = k // 2
    kb = k - ka
    if K == 1:
        return b, a
    if K == 2:
        return adi(b, 1)
    if n % 2 == 0:
        return adi(b, kb)
    else:
        if k % 2 == 0:
            return adi(a, ka)
        else:
            return adi(b, kb)
if __name__ == '__main__':
    main()
