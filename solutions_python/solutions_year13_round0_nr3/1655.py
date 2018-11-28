import bisect
# import json


def is_palindromes(num):
    num_str = str(num)
    l = len(num_str)
    i = 1
    ret = False
    while num_str[i - 1] == num_str[-i]:
        if i * 2 >= l:
            ret = True
            break
        i = i + 1
    return ret


def main():
    palindromes = set()
    result = []
    for i in range(1, 10000000):
        if i not in palindromes and not is_palindromes(i):
            continue
        palindromes.add(i)
        i_2 = i * i
        if is_palindromes(i_2):
            if i_2 < 10000000:
                palindromes.add(i_2)
            result.append(i_2)
    fout = open("output", "w")
    with open("input", 'r') as fin:
        test_case = int(fin.readline())
        for i in range(0, test_case):
            A, B = [int(x) for x in fin.readline().split()]
            a_pos = bisect.bisect_left(result, A)
            b_pos = bisect.bisect_right(result, B)
            print >> fout, "Case #%d: %d" % (i + 1, b_pos - a_pos)
            # print >> fout, a_pos, b_pos
            # print >> fout, result[a_pos:b_pos+1]


if __name__ == '__main__':
    main()
