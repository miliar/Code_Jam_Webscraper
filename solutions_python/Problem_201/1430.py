# https://code.google.com/codejam/contest/3264486/dashboard#s=p2
from collections import defaultdict

if __name__ == "__main__":
    filein = open('2017QC.in', 'r')
    fileout = open('2017QC.out', 'w')
    T = int(filein.readline())
    for t in range(T):
        fileout.write('Case #%d: ' % (t + 1))
        N, K = list(map(int, filein.readline().split()))

        current = defaultdict(int)
        current[N] = 1
        n, k, m = N, K, 1
        while k > m and n > 1:
            k -= m
            del current[n]
            if n > 1:
                if n % 2 == 1:
                    current[(n - 1) / 2] += 2 * m
                else:
                    current[n / 2] += m
                    if n > 2:
                        current[n / 2 - 1] += m
            # print(current.keys())
            n = max(current.keys())
            m = current[n]
        ans = ((n + 2) // 2 - 1, (n + 1) // 2 - 1)
        print(n)
        fileout.write('%d %d\n' % ans)

    filein.close()
    fileout.close()
