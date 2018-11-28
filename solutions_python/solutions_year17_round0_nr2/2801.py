with open('input.in', 'r') as fin:
    with open('output.out', 'w') as fout:
        T = int(fin.readline())
        for i in range(T):
            N = int(fin.readline())
            max = 1
            if str(N) == ''.join(sorted(str(N))):
                max = N
            else:
                for j in range(1, len(str(N))):
                    N //= pow(10, j)
                    N *= pow(10, j)
                    N += int('9' * j)
                    N -= pow(10, j)
                    if str(N) == ''.join(sorted(str(N))):
                        max = N
                        break
            fout.write('Case #%d: %d\n' % (i + 1, max))
