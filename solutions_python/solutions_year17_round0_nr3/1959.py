import math
# t = int(input())  # read a line with a single integer
# """ Use this for running a .in file on your pc.
file_x =  open('C-small-1-attempt0.in', 'r').readlines()
t = int(file_x[0])
# """
output_file = open('stall.txt', 'a')

def stall_decide(n, k):
    ls = 0
    rs = 0
    x_at = [0, n + 1]
    # print(x_at)
    """
    if n == k:
        return ls, rs
    """
    for i in range(k):
        v = [abs(x[1] - x[0]) for x in zip(x_at[1:], x_at[:-1])]
        z = v[:]
        v.sort()
        max_one = z.index(v[-1])
        max_two = z.index(v[-1]) + 1
        # print(max_one, max_two)
        # print(max_one, max_two)
        # max_diff = v[-1]


        # print(max_one, max_two, max_diff, x_at[max_one], x_at[max_two])

        new_x = x_at[max_one] + 1 + abs(int(((x_at[max_two] - 1)-(x_at[max_one] + 1))/2))

        x_at.append(new_x)
        x_at.sort()

        # print(x_at)

        if i == k - 1:
            ls = x_at[x_at.index(new_x)] - 1 - x_at[x_at.index(new_x) - 1]
            rs = x_at[x_at.index(new_x) + 1] - 1 - x_at[x_at.index(new_x)]

            if ls > rs:
                return ls, rs
            else:
                return rs, ls

for i in range(1, t + 1):
    # s, m = [int(s) for s in input().split(" ")]
    n, k = [(s1) for s1 in str(file_x[i]).split(" ")]
    y, z = stall_decide(int(n), int(k))
    # print("Case #{}: {} {}".format(i, y, z))
    output_file.write("Case #{}: {} {}\n".format(i, y, z))

output_file.close()