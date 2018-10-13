import sys
import os

def get_tidy_number(num):
    try:
        if num <= 1000:
            while num >= 0:
                num_str = str(num)
                max_digit = 0
                tidy_number = 0
                flag = 0
                for n in num_str:
                    if int(n) >= max_digit:
                        max_digit = int(n)
                    else:
                        flag = 1
                        break

                if flag:
                    num = num - 1
                else:
                    return num
        else:
            #TODO
            return num
            while num >= 1000:
                num_str = str(num)
                max_digit = 0
                tidy_number = 0
                flag = 0
                for n in num_str[::-1]:
                    if int(n) >= max_digit:
                        max_digit = int(n)
                    else:
                        flag = 1
                        break

                if flag:
                    num = num - 1
                else:
                    return num



            return num
    except Exception as e:
        print e


if __name__ == '__main__':
    i = 1
    if len(sys.argv) == 2:
        _file = sys.argv[1]
        fp = open(_file, 'r')
        lines = fp.readlines()
        T = lines[0]
        lines = lines[1:]
        for line in lines:
            out = get_tidy_number(int(line.strip()))
            print "Case #%s: %s"%(i, out)
            i += 1
    else:
        print "Enter T: "
        T = raw_input()
        print "Enter %s numbers: "
        in_list = list()
        while i <= int(T):
            num = raw_input()
            in_list.append(int(num))
            i += 1
        i = 1
        for num in in_list:
            out = get_tidy_number(int(num))
            print "Case #%s: %s"%(i, out)
            i += 1




