from collections import defaultdict

def test_case():
    N, K = map(int, input().split())
    stalls = defaultdict(int)
    stalls[N] = 1

    while K:
        length = max(stalls)
        num = stalls[length]
        del stalls[length]

        min_stalls = length // 2 - (length % 2 == 0)
        max_stalls = length // 2

        stalls[min_stalls] += num
        stalls[max_stalls] += num

        K -= num
        if K <= 0:
            return '{} {}'.format(max_stalls, min_stalls)
            

    print(K, N)

def main():
    T = int(input())
    for t in range(T):
        print('Case #{}:'.format(t + 1), test_case())

if __name__ == '__main__':
    main()
