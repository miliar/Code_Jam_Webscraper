YES = 'YES'
NO = 'NO'

def main():
    T = int(raw_input())
    t = 1
    while t <= T:
        nm = raw_input().split()
        N = int(nm[0])
        M = int(nm[1])

        n = 0
        data = []
        while n < N:
            data.append(map(int, raw_input().split()))
            n += 1

        rowMax = [0] * N
        colMax = [0] * M

        for i in range(N):
            for j in range(M):
                if data[i][j] > rowMax[i]:
                    rowMax[i] = data[i][j]

                if data[i][j] > colMax[j]:
                    colMax[j] = data[i][j]

        output = YES
        for i in range(N):
            for j in range(M):
                if data[i][j] < rowMax[i] and data[i][j] < colMax[j]:
                    output = NO

        print "Case #{}: {}".format(t, output)

        t += 1


if __name__ == "__main__":
    main()