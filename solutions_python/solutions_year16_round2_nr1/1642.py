def print_case_result(case_num, result):
    print "Case #" + str(case_num) +": " + str(result)


all_nums = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]



def convert_num_dict(origin_str):
        num_dict = dict()
        for c in origin_str:
                num = num_dict.get(c, 0)
                num += 1
                num_dict[c] = num
        return num_dict


def calc_all_num_dict():
        all_num_dicts = []
        for num in all_nums:
                all_num_dicts.append(convert_num_dict(num))
        return all_num_dicts


def cal_all_num_max(all_num_dicts, num_dict):
        num_max_count = []
        for each_num in all_num_dicts:
                min_count = None
                for n, c in each_num.items():
                        temp = num_dict.get(n, 0) / c
                        min_count = temp if min_count is None or temp < min_count else min_count
                num_max_count.append(min_count)
        return num_max_count

def  complete_dict(num_dict):
        for n,c in num_dict.items():
                if c > 0 :
                        return False
        return True

def do_solve(all_num_dicts,num_max_count, num_dict, num_count, cur_num):
        if complete_dict(num_dict):
                return True
        if cur_num == len(all_nums):
                return False
        cur_num_dict = all_num_dicts[cur_num]
        for i in range(num_max_count[cur_num]+1):
                can_use = True
                for n, c in cur_num_dict.items():
                        total = num_dict.get(n, 0) - c*i
                        if total < 0:
                                can_use = False
                                break
                if can_use:
                        for n, c in cur_num_dict.items():
                                total = num_dict.get(n, 0) - c*i
                                num_dict[n] = total
                        num_count[cur_num] = i
                        if  do_solve(all_num_dicts,num_max_count, num_dict, num_count, cur_num+1):
                                return True
                        num_count[cur_num] = 0
                        for n, c in cur_num_dict.items():
                                num_dict[n] = num_dict[n]  + c * i
        return False


def  solve(origin_str):
        num_dict = convert_num_dict(origin_str)
        all_num_dicts = calc_all_num_dict()
        num_max_count = cal_all_num_max(all_num_dicts, num_dict)
        num_count = [0] * len(all_nums)
        do_solve(all_num_dicts,num_max_count, num_dict, num_count, 0)
        ret = []
        for idx, n in enumerate(num_count):
                for _ in range(n):
                        ret.append(idx)
        return ''.join([str(i) for i in sorted(ret)])


if __name__ == '__main__':
    testcase_num = int(raw_input())
    for case_num in range(1, testcase_num+1):
        origin_str = raw_input().strip()
        ret = solve(origin_str)
        print_case_result(case_num, ret)
        