def set_element(arr, c_from, c_to, c_value):
    for idx in range(c_from, c_to):
        arr[idx] = c_value


def td_number_solver(last_number):
    last_number_arr = [int(e) for e in list(last_number)]
    number_size = len(last_number_arr)

    trailing_pivot = 0
    leading_pivot = number_size
    curr_pointer = number_size - 1

    while trailing_pivot < curr_pointer:
        curr_element = last_number_arr[curr_pointer]
        next_pointer = curr_pointer - 1
        next_element = last_number_arr[next_pointer]

        if next_element > curr_element:
            curr_pointer -= 1

            while trailing_pivot <= curr_pointer and last_number_arr[curr_pointer] <= 1:
                curr_pointer -= 1

            if curr_pointer <= trailing_pivot :
                curr_pointer = max(0, curr_pointer)
                last_number_arr[curr_pointer] -= 1

                if last_number_arr[curr_pointer] == 0:
                    trailing_pivot += 1
            else:
                last_number_arr[curr_pointer] -= 1

            curr_pointer += 1
            set_element(last_number_arr, curr_pointer, leading_pivot, 9)
            leading_pivot = curr_pointer

        curr_pointer -= 1


    return ''.join([str(a) for a in last_number_arr[trailing_pivot:]])


for idx in range(int(input())):
    case = input()
    res = td_number_solver(case)

    print("Case #%d: %s" % (idx + 1, res))