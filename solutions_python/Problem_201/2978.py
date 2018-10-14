f_name = "C-practice"
f_in = open(f_name + ".in", "r")
f_out = open(f_name + ".out", "w")

def pop_max_space(spaces):
    spaces.sort()
    m = spaces[len(spaces) - 1]

    return spaces[:-1], m

def split_max_space(v):
    v -= 1
    half = v // 2
    if 2*half == v:
        return half, half
    return half + 1, half

# for each test case
for test_case in range(int(f_in.readline().strip())):
    # read input
    n, k = list(map(int, f_in.readline().strip().split()))
    # init the spaces array
    spaces = [n]
    y, z = 0, 0
    # put each people
    for _ in range(k):
        # get the max space
        new_spaces, max_space = pop_max_space(spaces)
        y, z = split_max_space(max_space)
        spaces = new_spaces
        if y > 0:
            spaces.append(y)
        if z > 0:
            spaces.append(z)
    # print response
    f_out.write("Case #{}: {} {}\n".format(test_case+1, y, z))