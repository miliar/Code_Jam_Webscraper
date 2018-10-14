#! /usr/local/bin/python
# -*- coding:utf-8 -*-


def main():
    """
    inputをいれて
    outputを出力
    """
    for input_data in input_file():
        test_case, first_choice, first_arrange, second_choice,\
            second_arrange = input_data
        res = solve(first_choice, first_arrange, second_choice, second_arrange)
        output_file(test_case, res)
    return


def solve(first_choice, first_arrange, second_choice, second_arrange):
    """
    返り値
     -> 数値(１つに特定できた場合)
     -> "Bad magician!" (候補をしぼれなかった場合)
     -> "Volunteer cheated!" (候補が0にたった場合)
    """
    fisrt_candidate = set(first_arrange[first_choice-1])
    second_candidate = set(second_arrange[second_choice-1])
    sinter = fisrt_candidate & second_candidate
    slen = len(sinter)
    if slen == 1:
        return sinter.pop()
    elif slen == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"


def input_file():
    with open("./A-small-attempt0.in") as f:
        test_num = _trans_to_int(f.readline())

        for i in xrange(test_num):
            test_case = i + 1
            first_choice = _trans_to_int(f.readline())
            first_arrange = [[], [], [], []]
            for index in xrange(4):
                first_arrange[index] += _trans_to_int_list(f.readline())

            second_choice = _trans_to_int(f.readline())
            second_arrange = [[], [], [], []]
            for index in xrange(4):
                second_arrange[index] += _trans_to_int_list(f.readline())
            yield test_case, first_choice, first_arrange,\
                second_choice, second_arrange


def _trans_to_int(val):
    """
    "3\n" -> 3 に変換
    """
    val = val.rstrip()
    return int(val)


def _trans_to_int_list(val):
    """
    "1 2 3 4\n" -> [1, 2, 3, 4] に変換
    """
    val = val.rstrip("\n")
    int_list = []
    for num in val.split(" "):
        int_list.append(int(num))
    return int_list


def output_file(test_case, res):
    output_data = "Case #{x}: {y}\n".format(x=test_case, y=res)
    with open("./output", "a") as f:
        f.write(output_data)
    print output_data


if __name__ == "__main__":
    main()
