t = input()
t = int(t)

for casenum in range(1, t+1):

    d, n = input().split()
    d = int(d)
    n = int(n)

    longest_time_hrs = 0

    for i in range(n):

        k, s = input().split()
        k = int(k)
        s = int(s)

        km_remain = d - k
        time_remain_hrs = km_remain / s

        if (time_remain_hrs > longest_time_hrs):
            longest_time_hrs = time_remain_hrs


    result = d / longest_time_hrs

    print( 'Case #{}: {}'.format( casenum, result ) )
