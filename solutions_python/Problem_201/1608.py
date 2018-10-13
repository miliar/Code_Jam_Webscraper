import math

input = """100
5 1
5 2
5 3
5 4
5 5
"""

input = """100
5 1
5 2
5 3
5 4
5 5
"""

input = """100
4 2
5 2
6 2
1000 1000
1000 1
500000 237856
721296 626593
1000000 2
263513 215740
500000 237857
1000000 475712
2 1
999999 495446
816905 711834
1000000 524287
407295 332992
999999 127
500000 499999
999999 524288
4 1
452207 426486
611936 565186
646643 603626
339723 281929
1000000 500000
500000 250000
806009 667989
999999 475712
3 2
1000000 499998
384768 371816
828637 727609
500000 128
253638 192198
546629 541925
999999 128
2 2
267608 261508
3 1
806097 775889
632972 632330
1000000 480848
999999 453579
1000000 524288
999999 262144
423528 354749
294439 260227
999999 499997
484351 382203
500000 262144
1000000 128
1000000 475713
999999 999998
627720 590585
500000 127
1000000 1000000
999999 499999
500000 250792
500000 173911
498690 489175
514993 406282
500000 131072
688523 657752
500000 262143
992810 834677
999999 1
333349 304995
329792 256289
1000000 499999
756611 718064
1000000 127
574972 494054
440699 428840
1000000 262143
500000 500000
1000000 438677
361891 359236
776752 745186
500000 131071
999999 524287
434320 379041
999999 999999
999999 2
5 1
999999 499998
581738 488447
992164 894483
500000 2
999999 262143
667766 586306
500000 249998
1 1
932299 709745
999999 475711
500000 249999
500000 1
1000000 262144
1000000 999999
555816 418540
1000000 1
"""

def odd_divisor(x):
    return math.pow(2, (math.floor(math.log(x,2)) + 1))

def do_fast(N, K):
    if N == K:
        return [0,0]

    fast_odd = N // odd_divisor(K)


    # if N is even, then when K is powers of 2 need to add one to one of the values
    if N % 2 == 0:
        out_value_fast = [round(fast_odd - 1), round(fast_odd - 1)]

        if math.log(K,2) == math.floor(math.log(K,2)):
            out_value_fast[0] += 1
        return out_value_fast
    else:
        return [fast_odd, fast_odd]

def split(n):
    if n == 2:                          #inserted into two stalls, leaving one stall
        return [1]
    elif n == 1:                        #inserted into one stall, leaving no stalls
        return None
    elif n % 2 == 0:                    #even split
        return [n//2-1, n//2]
    else:                               #odd split
        return [(n-1)//2, (n-1)//2]

def custom_split(n):
    if n == 2:
        return [1, 0]
    elif n == 1:
        return [0, 0]
    elif n % 2 == 0:                    #even split
        return [n//2, n//2 - 1]
    else:                               #odd split
        return [(n-1)//2, (n-1)//2]

def better_method(N, K):
    current_values = custom_split(N)
    count = [1, 1]

    first = None
    second = None

    num_iterations = math.floor(math.log(K,2)) - 1
    # print('num iterations', num_iterations)

    for iterations in range(num_iterations):
        counter = {}

        for i, v in enumerate(current_values):
            scale = count[i]
            if v == 0:
                continue
                # if 0 in counter:
                #     counter[0] += count[i]
                # else:
                #     counter[0] = count[i]
            elif v == 1:
                if 0 in counter:
                    counter[0] += 1 * scale
                else:
                    counter[0] = 1 * scale
            else:
                two_numbers = custom_split(v)

                a = two_numbers[0]
                b = two_numbers[1]

                if a in counter:
                    counter[a] += 1 * scale
                else:
                    counter[a] = 1 * scale

                if b in counter:
                    counter[b] += 1 * scale
                else:
                    counter[b] = 1 * scale

        new_current_values = []
        new_count = []
        for keys, values in counter.items():
            new_count.append(values)
            new_current_values.append(keys)

        current_values = new_current_values
        count = new_count

        # print("values: {} ratio: {}".format(current_values, count))
        #
        if current_values[0] != 0:
             first = custom_split(current_values[0])
             if len(current_values) > 1:
                second = custom_split(current_values[1])
             # print("There will be {} {} and {} {}".format(count[0], first, count[1], second))

    number_1 = custom_split(N)
    number_2 = custom_split(max(number_1))
    number_3 = custom_split(min(number_1))

    if K == 1:
        return number_1
    elif K == 2:
        return number_2
    elif K == 3:
        return number_3
    else:
        relative_number = math.pow(2, num_iterations+ 1)
        fixed_number = K - relative_number + 1

        # print(relative_number)
        # print(fixed_number)
        if fixed_number > count[0]:
            return second
        else:
            return first


split_input = input.splitlines()

num_test_cases = split_input[0]
test_cases = split_input[1:]

#-1 == occupied
#None = not calculated

for test_case_i, test_case in enumerate(test_cases):
    # print("test case:", test_case)

    split_test_case = test_case.split()
    N = int(split_test_case[0])
    K = int(split_test_case[1])

    if False:
        stall_list = [N]

        for person_to_insert in range(K):
            #find the best one to pick
            best = -1
            best_i = -1
            for i, value in enumerate(stall_list):
                if value > best:
                    best = value
                    best_i = i

            # print('best position:', best_i, best)

            #remove that position and insert two more
            insert_values = split(stall_list[best_i])

            #insert at the 'best location'
            stall_list.pop(best_i)
            if insert_values:
                if len(insert_values) == 1:
                    stall_list.insert(best_i, 1)
                else:
                    stall_list.insert(best_i, insert_values[1])
                    stall_list.insert(best_i, insert_values[0])


        # print(stall_list)
        # print("output", insert_values)

        out_value = None
        if insert_values == None:
            out_value = [0,0]
        elif insert_values == [1]:
            out_value = [1,0]
        else:
            out_value = insert_values


        out_value_fast = better_method(N,K)#do_fast(N,K)

        pass_fail = False

        if out_value_fast == [max(out_value), min(out_value)]:
           pass_fail = True

        # print(out_value_fast)
        # better_method(N, K)

        # print(max(out_value), min(out_value))
        print("Case #{}: {} ({} {}) ({} {}) test:{}".format(test_case_i + 1, N / math.pow(2, 1 + math.floor(math.log(test_case_i+1,2))),max(out_value), min(out_value),out_value_fast[0], out_value_fast[1], pass_fail))
    else:
        result = better_method(N, K)
        print("Case #{}: {} {}".format(test_case_i + 1, max(result), min(result)))

# result = better_method(100, 31)
# print(result)