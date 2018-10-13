# find the largest integer with only inreasing numbers that is not greater than
# the one provided

def fix_number(number):
    prev = -1
    number_str = str(number)
    l = len(number_str)
    for i in range(l):
        if int(number_str[i]) < prev:
            # decrement and pad!
            part1 = fix_number(int(number_str[:i]) - 1)
            if part1 == "0":
                part1 = ""
            part2 = "9" * (l - i)
            return("%s%s" % (part1, part2))
        prev = int(number_str[i])

    return(number_str)

if __name__ == "__main__":
    test_count = int(raw_input())
    for i in range(test_count):
        number_str = raw_input()
        print("Case #%d: %s" % (i + 1, fix_number(number_str)))

#    print(fix_number(132))
#    print(fix_number(1000))
#    print(fix_number(7))
#    print(fix_number(111111111111111110))
