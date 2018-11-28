#! /usr/local/bin/python
# -*- coding:utf-8 -*-


def main():
    for input_data in input_file():
        res = solve(*input_data)
        output_file(*res)
    return


def solve(*args):
    test_case, C, F, X = args
    efficient = 2.
    total_time = 0.
    while True:
        # C個のcookie獲得時間
        item_second = C / efficient
        # 効率up時のX個のcookie獲得時間
        future_cookie_second = X / (efficient + F)
        # 現時点でのX個のcookie獲得時間
        current_cookie_second = X / efficient
        if item_second + future_cookie_second >= current_cookie_second:
            return test_case, total_time + current_cookie_second
        efficient += F
        total_time += item_second
        continue


def input_file():
    with open("./B-large.in") as f:
        test_num = _trans_to_int(f.readline())

        for i in xrange(test_num):
            test_case = i + 1
            C, F, X = _trans_to_float_list(f.readline())
            yield test_case, C, F, X


def _trans_to_int(val):
    """
    "3\n" -> 3 に変換
    """
    val = val.rstrip()
    return int(val)


def _trans_to_float_list(val):
    """
    "30.0 1.0 2.0\n" -> [30. 1. 2.] に変換
    """
    val = val.rstrip("\n")
    float_list = []
    for num in val.split(" "):
        float_list.append(float(num))
    return float_list


def output_file(*args):
    output_data = "Case #{x}: {y}\n".format(x=args[0], y=round(args[1], 7))
    with open("./output", "a") as f:
        f.write(output_data)
    return


if __name__ == "__main__":
    main()
