import operator

# read
def file_read(input_file, output_file):
    with open(input_file, "r") as fin:
        with open(output_file, "w") as fout:
            num_test_cases = int(fin.readline())
            for i in range(num_test_cases):
                xy = fin.readline().rstrip().split()
                x = int(xy[0])
                y = int(xy[1])
                list_int = []
                for ii in range(x):
                    str_list = fin.readline().rstrip().split()
                    list_int.extend([int(s) for s in str_list])
                
                check = is_cutable(x, y, list_int)
                print check
                msg = "YES" if check else "NO"
                fout.write("Case #{num}: {msg}\n".format(num=i+1, msg=msg))


file_read("B-large.in", "out_b.txt")

def itemgetter_index(x, y):
    ret = []
    for i in range(x):
        ret.append([i*y + jj for jj in range(y)])
    for j in range(y):
        ret.append([j + ii*y for ii in range(x)])
    return ret
def check_line(target, list_int):
    is_line = True

    for i in list_int:
        is_line = is_line and (i == 'x' or i == target)
    return is_line

def check_graph(getters, target, list_int):
    # check if graph ok
    for getter in getters:
        print getter
        line_getter = operator.itemgetter(*getter)
        list_line = line_getter(list_int)

        if isinstance(list_line, int):
            list_line = [list_line]
        else:
            list_line = list(list_line)

        if check_line(target, list_line):
            for index in getter:
                list_int[index] = 'x'
    return not target in list_int
def is_cutable(x, y, list_int):
    # values
    getters = itemgetter_index(x, y)
    vals = sorted(set(list_int))
    for v in vals:
        if not check_graph(getters, v, list_int):
            return False
    return True


#print itemgetter_index(9, 2)

