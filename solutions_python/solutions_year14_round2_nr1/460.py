import time
import sys

file_in = file('test.in', 'r')
file_out = file('test.out', 'w')

def main():
    n_case = int(file_in.readline())
    for case in range(1, n_case + 1):
        solveCase(case)

def reduced(s):
    result = []
    i = 0
    while i < len(s):
        count = 0
        while (i + 1 < len(s)) and (s[i + 1] == s[i]):
            i += 1
            count += 1
        result.append((s[i], count + 1))
        i += 1
    return result

def solveCase(case_number):
    print '----'
    #in
    n_str = int(file_in.readline())

    #main
    str_list = [''] * n_str
    char_count = []
    # reduced_len = 0
    print n_str
    for i in range(n_str):
        str_list[i] = file_in.readline().strip()
        # print str_list[i]

    for i in range(n_str):
        str_list[i] = reduced(str_list[i])
        print i
        reduced_len = len(str_list[i])

        if i > 0 and (len(str_list[i]) != len(str_list[i - 1])):
            file_out.write("Case #" + repr(case_number) + ": Fegla Won\n")
            return

        char_count.append([])
        for j in range(len(str_list[i])):
            if i > 0 and str_list[i][j][0] != str_list[i - 1][j][0]:
                file_out.write("Case #" + repr(case_number) + ": Fegla Won\n")
                return

    result = 0
    for i in range(reduced_len):
        sorted_char_count = sorted(map(lambda arr: arr[i][1], str_list))
        print sorted_char_count
        
        if n_str % 2 == 0:
            median = int((sorted_char_count[(n_str - 1) / 2] + sorted_char_count[(n_str - 1) / 2 + 1]) / 2.0)
        else:
            median = sorted_char_count[n_str / 2]
        # print 'median', median
        for char_count in sorted_char_count:
            result += abs(char_count - median)

    #out
    file_out.write("Case #" + repr(case_number) + ": " + repr(int(result)) + "\n")


if __name__ == '__main__':
    startTime = time.clock()
    main()
    print (time.clock() - startTime)