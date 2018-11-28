def func(R, k, N, groups):

    def inc(x):
        return x+1 if not x == N - 1 else 0

    money_sum = 0
    current_group = 0
    for x in range(R):
        amount = 0
        groups_in_set=0
        while True:
            if(amount + groups[current_group] <= k and groups_in_set + 1 <= N):
                amount+=groups[current_group]
                money_sum += groups[current_group]
                current_group = inc(current_group)
                groups_in_set +=1
            else:
                break
    return money_sum

in_file = open('in', 'r')
out_file = open('out', 'w')

T = int(in_file.readline())

for i in range(T):
    s = in_file.readline()
    R, k, N = tuple([int(x) for x in s.split()])

    s = in_file.readline()
    groups = [int(x) for x in s.split()]

    case = 'Case #%d: ' % (i +1)
    case+=str(func(R, k, N, groups)) + "\n"
    out_file.writelines(case)

