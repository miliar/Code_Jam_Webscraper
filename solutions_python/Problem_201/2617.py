"""
Problem

A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends
are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other
people as possible. To avoid confusion, they follow deterministic rules:
For each empty stall S, they compute two values LS and RS, each of which is the number of
empty stalls between S and the closest occupied stall to the left or right, respectively.
Then they consider the set of stalls with the farthest closest neighbor, that is, those S
for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise,
they choose the one among those where max(LS, RS) is maximal.
If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives.
Nobody will ever leave.

When the last person chooses their stall S, what will be the values of max(LS, RS) and min(LS, RS) be?

Solving this problem

This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset
before you can attempt the second Small dataset. You will be able to retry either of the Small
datasets (with a time penalty). You will be able to make a single attempt at the Large,
as usual, only after solving both Small datasets.

Input

The first line of the input gives the number of test cases, T. T lines follow.
Each line describes a test case with two integers N and K, as described above.

Output

For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1),
y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.

Limits

1 <= T <= 100.
1 <= K <= N.
Small dataset 1

1 <= N <= 1000.

Input

5
4 2
5 2
6 2
1000 1000
1000 1


Output

Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499

"""

input_file_name = 'C-small-1-attempt0.in'
output_file_name = 'C-small-1-attempt0.out'

f = open(input_file_name, 'r')
outFile = open(output_file_name, 'w', 0)

# get T, the number of test cases
T = f.readline()
T = int(T)
for t in range(T):
    print '---------------------'
    line = f.readline()
    N, K = line.split()
    K = int(K)
    N = int(N)
    print 'N: {}, K: {}'.format(N, K)
    if N < 10000:
        stalls = []
        stalls.append('O')
        for n in range(N):
            stalls.append('.')
        stalls.append('O')
        # print 'stalls: {}'.format(stalls)

        for k in range(K):
            # print 'k = {}'.format(k)
            mins = []
            maxes = []
            maxMax = -1
            maxMin = -1
            # check all empty stalls
            for s in range(1, N+1):
                # calculate LS and RS for each empty stall
                if stalls[s] != 'O':
                    LS = 0
                    l = s-1
                    while l > 0 and stalls[l] != 'O':
                        LS+=1
                        l-=1
                    # print 'LS for S={} is {}'.format(s, LS)
                    RS = 0
                    r = s+1
                    while s < N:
                        if stalls[r] != 'O':
                            RS+=1
                            r+=1
                        else:
                            break
                    # print 'RS for S={} is {}'.format(s, RS)
                    minimum = min(LS, RS)
                    if minimum > maxMin:
                        maxMin = minimum

                    maximum = max(LS, RS)
                    if maximum > maxMax:
                        maxMax = maximum

                    result = (minimum, maximum, s)
                    mins.append(result)

            # print 'mins: {}'.format(mins)

            # group the maximal mins together
            maximalMins = []
            for m in mins:
                if m[0] == maxMin:
                    maximalMins.append(m)

            # print 'maximalMins: {}'.format(maximalMins)

            if len(maximalMins) == 0:
                # k chooses this stall
                m = maximalMins[0]
                selected = m[2]
                # print 'selected stall: {}'.format(selected)
                y = m[1]
                z = m[0]
                # print 'y = {}, z = {}'.format(y, z)
                stalls[selected] = 'O'

            # if there is more than one maximal min, find the maximal max of the maximalMins
            else:
                maxOfMins = -1
                for m in maximalMins:
                    if m[1] > maxOfMins:
                        maxOfMins = m[1]

                maximalMaxes = []
                for m in maximalMins:
                    if m[1] == maxOfMins:
                        maximalMaxes.append(m)

                # print 'maximalMaxes: {}'.format(maximalMaxes)
                if len(maximalMaxes) == 0:
                    # k chooses this stall
                    m = maximalMaxes[0]
                    selected = m[2]
                    # print 'selected stall: {}'.format(selected)
                    y = m[1]
                    z = m[0]
                    # print 'y = {}, z = {}'.format(y, z)
                    stalls[selected] = 'O'
                else:
                    # k chooses the left-most stall
                    leftMost = N+2
                    for m in maximalMaxes:
                        if m[2] < leftMost:
                            leftMost = m[2]

                    selected = leftMost
                    # print 'selected stall: {}'.format(selected)
                    y = m[1]
                    z = m[0]
                    # print 'y = {}, z = {}'.format(y, z)

                    stalls[selected] = 'O'

            # print 'stalls: {}'.format(stalls)
            if k == (K-1):
                output = 'Case #{}: {} {}'.format((t+1), y, z)
                print output
                outFile.write(output + "\n")
