def testcase():
    n = (input())
    digitsCount = len(str(n))

    dp = [[[0 for _ in range(2)] for _ in range(10)] for _ in range(digitsCount)]

    for d_index in range(digitsCount):
        for d in range(10):
            # ends
            # dp[d_index][d][0] --> how many tidy numbers of length d_index that ends with d and went below
            # dp[d_index][d][1] --> how many tidy numbers of length d_index that ends with d and did not go below
            if d_index == 0:
                if d == int(n[d_index]):
                    dp[0][d][1] = d
                else:
                    if d < int(n[d_index]):
                        dp[0][d][0] = d

                continue

            # doing 0

            # case 1: was under before
            dp[d_index][d][0] = max([dp[d_index-1][d_prev][0] for d_prev in range(d+1)]) * 10 + d

            #case 2: just went under
            if d < int(n[d_index]):
                dp[d_index][d][0] = max(dp[d_index][d][0], max([dp[d_index-1][d_prev][1] for d_prev in range(d+1)])*10 + d)

            #case 3: stayed on the line
            if d == int(n[d_index]):
                dp[d_index][d][1] = max(dp[d_index][d][1], max([dp[d_index-1][d_prev][1] for d_prev in range(d+1)])*10 + d)

    return max(dp[digitsCount-1][d][state] for d in range(10) for state in range(2))


t = int(input())

for num in range(t):
    print("Case #{num}: {result}".format(num=num + 1, result=testcase()))
