# imports
import sys, re

def main(filename):
    # open file
    f_in = open(filename, "r")
    # return array of lines
    lines = f_in.readlines()
    # close file
    f_in.close()

    f_out = open("%s.out" % filename, "w")
    use_case_count = int(lines.pop(0))
    current_use_case_num = 0
    result = 0
    for line in lines:
        if current_use_case_num > use_case_count:
            break
        else:
            current_use_case_num += 1

        s = list(str(line.rstrip()))
        flag = True
        while flag:
            count = 0
            for index, item in enumerate(s):
                item = str(item)
                item = int(item)
                if index + 1 < len(s) and item > int(s[index + 1]):
                    result = int("".join(s)) - 1
                    s = list(str(result))
                    break
                else:
                    result = int("".join(s))
                count += 1

            if count == len(s):
                flag = False
                break
        f_out.write("Case #%s: %s\n" % (str(current_use_case_num), str(result)))
    f_out.close()

main("./B-small-attempt0.in")


