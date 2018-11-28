def to_num_list(num):
    return map(lambda x: int(x), list(str(num)))


def to_num(l_num):
    return int("".join(map(lambda x: str(x), l_num)))
    

def check(num_list):
    if num_list == sorted(num_list):
        return True
    return False


def dumb_check(num):
    thing = list(str(num))
    if thing == sorted(thing):
        return True
    return False


def fix(l_num, place):
    l_num[place] = l_num[place] - 1
    l_num[(place+1):(len(l_num))] = [9]*(len(l_num)-(place+1))


def single_pass(l_num):
    for i in range(len(l_num)-1):
        if l_num[i] > l_num[i+1]:
            fix(l_num, i)


def brute_force(num):
    res = num
    while not dumb_check(res):
        res = res - 1
    return res


def solve(num):
    l_num = to_num_list(num)
    while not check(l_num):
        single_pass(l_num)
    return to_num(l_num)


def solve_for_file(file_loc, o_loc, check_with_brute=False):
    count = 0
    with open(file_loc, "r") as f:
        with open(o_loc, "w") as o:
            for line in f:
                if count > 0:
                    solution = solve(int(line))
                    if check_with_brute:
                        bf_solution = brute_force(int(line))
                        if bf_solution != solution:
                            print "Oh fuck"
                    o.write("Case #%d: " % count)
                    o.write(str(solution))
                    o.write("\n")
                count += 1

                
solve_for_file("real_big_dat.txt", "real_big_out.txt")

