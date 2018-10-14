# Google Code Jam 2017 QB
# Replace every digit with first digit.  If > limit, replace first
# digit with one less and other digits with nines and done.  Else, record
# first digit and recurse on rest of number.
def solve(limit):
    if len(limit) == 1: return limit
    if int(limit[0] * len(limit)) > int(limit):
        return str(int(limit[0])-1) + '9' * (len(limit) - 1)
    else:
        return limit[0] + solve(limit[1:])

cases = int(raw_input())
for i in range(cases):
    print 'Case #{}: {}'.format(i+1, int(solve(raw_input().strip())))

