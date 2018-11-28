#include <cstdio>

tidy = [];

for i in range(1, 10):
    tidy.append(str(i))

prev = 0;
for digit in range(2, 19):
    start = prev
    end = len(tidy)
    for i in range(start, end):
        for j in range(1, int(tidy[i][0])+1):
            tidy.append(str(j) + tidy[i])
    prev = end

tidy = [int(S) for S in tidy]
tidy = sorted(tidy)

cases = input()
for caseNum in range(1, cases+1):
    N = input();

    left = 0
    right = len(tidy)
    while left < right:
        mid = (left + right) / 2

        if tidy[mid] > N:
            right = mid
        else:
            left = mid

        if (left + right) / 2 == mid:
            break

    print('Case #{}: {}'.format(caseNum, tidy[left]))
