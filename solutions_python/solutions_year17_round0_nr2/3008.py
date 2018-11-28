import sys


def get_dip_index(num_as_str):
    old_ch = '-'
    for index, ch in enumerate(num_as_str):
        if old_ch != '-' and ch < old_ch:
            return index
        old_ch = ch
    return -1


def largest_tidy(numstr):
    dip_index = get_dip_index(numstr)
    if dip_index == -1:
        # This number is already tidy
        return numstr
    if numstr[dip_index - 1] == '1':
        # If the digit before the pivot is 1, all the leading digits of the number must have been 1.
        # The highest tidiest number is all 9s with fewer digits
        return '9' * (len(numstr) - 1)
    else:
        decreased_digit = str(int(numstr[dip_index - 1]) - 1)
        trailing_nines = '9' * (len(numstr) - dip_index)
        candidate = numstr[:dip_index - 1] + decreased_digit + trailing_nines
        if get_dip_index(candidate) == -1:
            return candidate
        else:
            return largest_tidy(candidate)


def main(filename):
    # print "Reading from: ", filename
    with open(filename) as f:
        num_entries = int(f.readline())
        for i in range(num_entries):
            solution = largest_tidy(f.readline().strip())
            print "Case #" + str((i + 1)) + ": " + str(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "You should provide the input file name"
    else:
        main(sys.argv[1])
