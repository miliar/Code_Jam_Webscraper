import sys


def checkTidyRec(org, current, pos, nine):
    if pos >= len(org):
        return True, current
    elif nine:
        current.append(9)
        return checkTidyRec(org, current, pos+1, nine)
    elif org[pos] >= current[pos-1]:
        current.append(org[pos])
        res_bool, res = checkTidyRec(org, current, pos+1, False)
        if res_bool:
            return True, res

        current[pos] = org[pos] - 1
        if current[pos] >= current[pos-1]:
            return checkTidyRec(org, current, pos+1, True)
        else:
            return False, None
    elif org[pos] < current[pos-1]:
        # The current path cannot work
        return False, None


def checkTidy(last_num, case):
    num_list = [int(x) for x in list(str(last_num))]
    current = [num_list[0]]
    res_bool, res = checkTidyRec(num_list, current, 1, False)
    if res_bool:
        if res[0] == 0:
            res = res[1:]
        output = "".join([str(x) for x in res])
    else:
        current = [num_list[0]-1]
        _, res = checkTidyRec(num_list, current, 1, True)
        if res[0] == 0:
            res = res[1:]
        output = "".join([str(x) for x in res])

    return "Case #" + str(case) + ": " + output + "\n"


def pancake(input, output):
    # Read input
    with open(output, "w") as o:
        with open(input, "r") as f:
            f.readline() # Read number of examples
            # Process examples
            i = 1
            for line in f:
                o.write(checkTidy(int(line), i))
                i += 1


if __name__ == '__main__':
    pancake(sys.argv[1], sys.argv[2])
