import sys

def read_input(infile):
    count = 0
    in_cases = []
    with open(infile, 'r') as f:
        lines = f.readlines()
        count = int(lines[0])
        for i in range(count):
            in_cases.append(int(lines[i+1]))

    return in_cases


# used for small input set only
def is_non_decreasing(inp):
    digit_str = str(inp)
    l = len(digit_str)
    if l==1:
        return True
    d_prev = 9
    for i, d in enumerate(digit_str[::-1]):
        d = int(d)
        if i == 0:
            d_prev = d
            continue
        else:
            if d<=d_prev:
                if i==l-1:
                    return True
                else:
                    d_prev = d
                    continue
            else:
                return False
    return False


# can be used for small and large both sets
def find_largest_tidy_number(n):
    numstr = str(n)
    num_digits = len(numstr)
    if num_digits == 1:
        return n
    n_min = int(''.join(['1' for i in range(num_digits)]))
    n_max = int(''.join(['9' for i in range(num_digits)]))
    if n_min == n or n_max == n:
        return n
    elif n_min > n:
        n_tidy = ['9' for i in range(num_digits-1)]
        return int(''.join(n_tidy))
    else:
        d_prev = 9
        tidy_num = [s for s in numstr]
        # check the leftmost digit not satisfying the condition, and replace it with its right digit, then all further right digits as 9
        for i, d in enumerate(numstr):
            d = int(d)
            if i == 0:
                d_prev = d
                continue
            if d >= d_prev:
                if i==num_digits-1:
                    return n
                else:
                    d_prev = d
                    continue
            else:
                found = False
                while not found:
                    for y in range(i, 0, -1):
                        tidy_num[y-1] = str(int(tidy_num[y-1])-1)
                        for x in range(y, num_digits):
                            tidy_num[x] = '9'
                        val = int(''.join(tidy_num))
                        found = is_non_decreasing(val)
                        if found:
                            break
                return int(''.join(tidy_num))


def solve(in_cases, outfile):
    for index,case in enumerate(in_cases):
        print(index,case)
        tidy_num = find_largest_tidy_number(case)
        #found = False
        #while not found:
            #found = is_non_decreasing(case)
        with open(outfile, 'a') as f:
            f.write("Case #%s: %s\n" %(index+1, tidy_num))
    return 


if __name__ == "__main__":
    filename = sys.argv[1]
    outfile = sys.argv[2]
    in_cases = read_input(filename)
    print(in_cases)
    solve(in_cases, outfile)

