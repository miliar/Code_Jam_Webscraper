def number_of_flips(need_to_do, s, k):
    n_flips = 0
    will_do = 0
    pan = 2 ** k - 1
    for i in range(s - k + 1):
        flip = pan * 2 ** i
        if need_to_do & (2 ** i) != will_do & (2 ** i):
            will_do ^= flip
            n_flips += 1
    if will_do == need_to_do:
        return n_flips
    return False

def string_state_to_need_to_do_num(current_state_string):
    num = 0
    for i in range(len(current_state_string)):
        if current_state_string[i] == '-':
            num += 2 ** i
    return num

def get_answer(current_state_string, k):
    s = len(current_state_string)
    result = number_of_flips(string_state_to_need_to_do_num(current_state_string), s, k)
    if result is not False:
        return result
    else:
        return "IMPOSSIBLE"

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    current_state_string, k = [s for s in input().split(" ")]
    k = int(k)
    print("Case #{}: {}".format(i, get_answer(current_state_string, k)))


