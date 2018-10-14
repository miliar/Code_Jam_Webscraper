if __name__ == '__main__':
    t = int(input().strip())
    for tests in range(1, t + 1):
        n, k = list(map(int, input().split()))
        A = [0 for x in range(n+2)]
        A[0]=1
        A[n+1]=1
        a = 0
        b = 0
        for i in range(1, k+1):
            div = []
            for j in range(0, len(A)):
                if A[j]:
                    div.append(j)
            maxs = -1
            maxl = 0
            maxr = 0
            for m in range(1, len(div)):
                diff = div[m] - div[m-1]
                if diff > maxs:
                    maxs = diff
                    maxl = div[m-1]
                    maxr = div[m]
            mid = int((maxr-maxl) / 2) + maxl
            A[mid] = 1
            if maxr == maxl+1:
                a = b = 0
            else:
                a = mid - maxl - 1
                b = maxr - mid - 1


        # A = []
        # kk = k
        # nn = n
        #
        # while  kk > 1:
        #     d = kk % 2
        #     A.append(d) # 0 right, 1 left
        #     if not d:
        #         kk = int(kk/2)
        #     else:
        #         kk = int((kk-1) / 2)
        #     #kk -= 1
        # #print(n, k, nn, kk, A)
        # A = A[::-1]
        #
        # l = 0
        # r = n+1
        # #print(A)
        # for j in A:
        #     m = int((r-l) / 2) + l
        #     if j:
        #         r = m
        #     else:
        #         l = m
        # mm = int((r-l) / 2) + l
        # #print(l, r, mm)
        # if r == l+1:
        #     a = b = 0
        # else:
        #     a = mm - l - 1
        #     b = r - mm - 1

        print("Case #{test}: {y} {z}".format(test=tests, y=max(a, b), z=min(a,b)))