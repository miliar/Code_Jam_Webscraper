t = int(raw_input())  # read a line with a single integer
for task in xrange(1, t + 1):
    NA,NB = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    A = []
    B = []
    for i in range(0, NA):
        A.append([int(s) for s in raw_input().split(" ")])
    for i in range(0, NB):
        B.append([int(s) for s in raw_input().split(" ")])

    A.sort()
    B.sort()

    A_sum = 0
    B_sum = 0
    for a in A:
        A_sum += a[1] - a[0]
    for b in B:
        B_sum =+ b[1] - b[0]

    ans = -1
    if len(A) == 0:
        if len(B) == 1:
            ans = 2
        else:
            if B_sum == 720:
                ans = 4
            elif B[0][0] >= 720 and B[1][0] >= 720:
                ans = 2
            elif B[0][1] <= 720 and B[1][1] <= 720:
                ans = 2
            elif B[1][1] - B[0][0] <= 720:
                ans = 2
            elif B[0][1] + (1440 - B[1][0]) <= 720:
                ans = 2
            else:
                ans = 4

    elif len(B) == 0:
        if len(A) == 1:
            ans = 2
        else:
            if A_sum == 720:
                ans = 4
            elif A[0][0] >= 720 and A[1][0] >= 720:
                ans = 2
            elif A[0][1] <= 720 and A[1][1] <= 720:
                ans = 2
            elif A[1][1] - A[0][0] <= 720:
                ans = 2
            elif A[0][1] + (1440 - A[1][0]) <= 720:
                ans = 2
            else:
                ans = 4
    else:
        ans = 2



    print "Case #{}: {}".format(task, ans)
