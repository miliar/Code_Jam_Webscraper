def solve(field):
    c_all = [[field[x][j] for x in xrange(len(field))] for j in xrange(len(field[0]))]

    r_max = [max(x) for x in field]  # max values in rows
    c_max = [max(x) for x in c_all]  # max values in col...
    # print c_all
    # print field
    # print r_max
    # print c_max
    for i in xrange(len(field)):
        for j in xrange(len(field[i])):
            val = field[i][j]
            # print i,j,r_max,c_max
            if val != r_max[i] and val != c_max[j]:
                return "NO"
    return "YES"


def parse():
    with open("input", "r") as f_in, open("output", "w") as f_out:
        total_cases = int(f_in.readline())
        for case_num in xrange(total_cases):
            height = f_in.readline().strip()
            t_n = int(height.split()[0])
            # print t_n
            problem = []

            for n in xrange(t_n):
                nums = [int(x.strip()) for x in f_in.readline().split()]
                problem.append(nums)
            # print case_num+1
            # print problem
            out_string = "Case #{}: {}".format(case_num + 1, solve(problem))
            # print out_string
            f_out.write(out_string + "\n")

if __name__ == '__main__':
    parse()
