# Problem A. Oversized Pancake Flipper


def ordered(num_list, num_len):
    for idx in range(num_len - 1):
        if num_list[idx] > num_list[idx + 1]:
            return False, idx
    return True, 0


def solve(num_str):
    num_list = list(num_str)
    num_len = len(num_list)

    idx = num_len - 1
    while idx > 0:
        rst, idx = ordered(num_list, num_len)

        if rst:
            break
        else:
            num_list[idx] = str(int(num_list[idx]) - 1)
            for remain in range(idx + 1, num_len):
                num_list[remain] = '9'

    if num_list[0] == '0':
        num_list.remove(num_list[0])

    return ''.join(num_list)


def main():
    #inputFile = "B-small-attempt0.in"
    #inputFile = "B-small-attempt2.in"
    inputFile = "B-large.in"
    outFile = inputFile + ".out"

    inpf = open(inputFile, "r")
    outf = open(outFile, "w")

    test_case = int(inpf.readline())

    #false_msg = "IMPOSSIBLE"

    for case in range(test_case):

        nums = inpf.readline().strip()

        num = solve(nums)

        result = 'Case #{}: {}\n'.format(case + 1, num)

        print(result, end='')
        outf.write(result)
    inpf.close()
    outf.close()





if __name__ == "__main__":
    main()
    #num = solve('228')
    #print(num)