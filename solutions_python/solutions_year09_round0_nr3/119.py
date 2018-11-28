#!/usr/bin/env python

def solve(input):
    codejam = "welcome to code jam";

    dp = [[0 for _ in range(len(input))] for _ in range(len(codejam))]

    for j in range(len(input)):
        if input[j] == codejam[0]:
            dp[0][j] = 1

    for i in range(1, len(codejam)):
        for j in range(len(input)):
            if input[j] == codejam[i]:
                dp[i][j] = sum(dp[i-1][:j])

    return "%04d" % (sum(dp[-1]) % 10000)

if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        print "Case #%d:" % (i+1), solve(raw_input())
