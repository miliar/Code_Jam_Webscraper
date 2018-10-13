from collections import defaultdict
import sys

def _get_divides(num):
    yield [(num/2 + num % 2),(num/2)]
    if num % 3 == 2:
        yield [num/3, num/3, (num/3+1)]
    elif num % 3 == 1:
        yield [num/3, (num/3+1), (num/3+1)]
    else:
        yield [num/3, num/3, num/3]

def get_result(arr_counter, number_of_minutes):
    all_keys = set(arr_counter.keys())
    max_number = max(all_keys)
    all_keys.remove(max_number)
    next_max = max(all_keys) if all_keys else 0
    divide_numbers =  _get_divides(max_number)
    max_steps = sys.maxint

    if max_number < 4:
        return number_of_minutes + max_number

    #check no divide
    max_steps = min(max_steps, number_of_minutes + max_number)

    for possible_divide in divide_numbers:
        split_minutes = (len(possible_divide)-1)*arr_counter[max_number]
        new_number_of_minutes = number_of_minutes + split_minutes
        new_arr = arr_counter.copy()
        for n in possible_divide:
            new_arr[n] += 1
        del new_arr[max_number]
        max_steps = min(get_result(new_arr, new_number_of_minutes), max_steps)
    return max_steps

    #
    #
    #
    #
    #     max_after_split = max(next_max, max(possible_divide))
    #     if split_minutes + max_after_split >= max_number:
    #         max_steps = min(max_number + number_of_minutes, max_steps)
    #         continue
    #     else:
    #         new_number_of_minutes = number_of_minutes + split_minutes
    #         new_arr = arr_counter.copy()
    #         for n in possible_divide:
    #             new_arr[n] += 1
    #         del new_arr[max_number]
    #         max_steps = min(get_result(new_arr, new_number_of_minutes), max_steps)
    #
    # return max_steps


cases = int(raw_input())
for case in range(1, cases+1):
    d = int(raw_input())
    arr_counter = defaultdict(int)
    arr = map(int, raw_input().split(" "))
    for num in arr:
        arr_counter[num] += 1
    print ("Case #%s: %s" % (case, get_result(arr_counter, 0)))



    # number_of_minutes = 0
    # finished = False
    # while not finished:
    #     max_number = max(arr_counter.keys())
    #
    #
    #     biggest_group = (max_number / 2) + (max_number % 2)
    #
    #     if biggest_group + arr_counter[max_number] >= max_number:
    #         finished = True
    #         number_of_minutes += max_number
    #     else:
    #         number_of_minutes += arr_counter[max_number]
    #         big_div = (max_number / 2) + (max_number % 2)
    #         small_div = (max_number / 2)
    #         arr_counter[big_div] += arr_counter[max_number]
    #         arr_counter[small_div] += arr_counter[max_number]
    #         del arr_counter[max_number]
    #print("Case #%s: %s" % (case, number_of_minutes))

    #
    # for num in arr:
    #
    #
    #
    #
    # max_t, t_array = raw_input().split(" ")
    # number_of_people = 0
    # number_to_add = 0
    # for i, num in enumerate(t_array):
    #     num = int(num)
    #     if number_of_people < i:
    #         temp_number_to_add = i - number_of_people
    #         number_to_add += temp_number_to_add
    #         number_of_people += temp_number_to_add
    #     number_of_people += num
    # print("Case #%s: %s" % (case, number_to_add))