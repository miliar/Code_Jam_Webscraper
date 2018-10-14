import sys

if __name__=='__main__':
    n = int(sys.stdin.readline())
    for i in range(n):
        sys.stdout.write("Case #{}: ".format(i + 1))
        n, m = map(int, sys.stdin.readline().split(' '))
        files = sorted(map(int, sys.stdin.readline().split(' ')))
        i, j = 0, len(files) - 1
        p = 0
        while(i < j):
            if files[i] + files[j] <= m:
                i += 1
                j -= 1
                p += 1
            else:
                j -= 1
                p += 1
        if i == j:
            p += 1
        ans = p
        sys.stdout.write("{}\n".format(ans))

