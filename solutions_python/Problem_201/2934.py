

def calc_stall_probs(stalls, toilet_index):

    # Go left
    left_count = 0
    right_count = 0
    i = toilet_index
    keep_going = True
    while i !=0 and keep_going:
        if stalls[i-1] == False:
            left_count += 1
        else:
            keep_going = False
        i -= 1

    i = toilet_index
    keep_going = True
    while i != (len(stalls) - 1) and keep_going:
        if stalls[i + 1] == False:
            right_count += 1
        else:
            keep_going = False
        i +=1

    return left_count, right_count

def select_stall(stall_selector, stall_probs):
    max_val = max(stall_selector)
    indices = [i for i, x in enumerate(stall_selector) if x == max_val]
    if len(indices) == 1:
        return indices[0]

    lst = []
    for check_id in range(len(indices)):
        lst.append(-1)
        lst[check_id] = max(stall_probs[indices[check_id]]['right'], stall_probs[indices[check_id]]['left'])

    max_val2 = max(lst)
    indices2 = [i for i, x in enumerate(lst) if x == max_val2]

    if len(indices2) == 1:
        return indices[indices2[1]]
    else:
        return indices[indices2[0]]


def fill_toilets(stalls, num_people):

    toilet_stalls = []

    ans_ret_left = -1
    ans_ret_right = -1
    for i in range(stalls):
        toilet_stalls.append(False)
    toilet_stalls[0] = True
    toilet_stalls[len(toilet_stalls) - 1] = True

    for i in range(num_people):
        #print toilet_stalls
        stall_probs = []
        stall_selector = []
        for stall_check in range(stalls):
            # Stall is empty
            probs = {'left': -1, 'right': -1}
            stall_probs.append(probs)
            stall_selector.append(-1)
            if toilet_stalls[stall_check] == False:
                l, r = calc_stall_probs(toilet_stalls, stall_check)
                stall_probs[stall_check]['left'] = l
                stall_probs[stall_check]['right'] = r
                stall_selector[stall_check] = min(l,r)
        #print stall_probs
        #print stall_selector
        choose_idx = select_stall(stall_selector, stall_probs)
        #print choose_idx
        ans_ret_left = stall_probs[choose_idx]['left']
        ans_ret_right = stall_probs[choose_idx]['right']
        #print stall_probs[choose_idx]
        toilet_stalls[choose_idx] = True

    #print toilet_stalls
    return ans_ret_left, ans_ret_right


# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    m, n = [long(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    ans1, ans2 = fill_toilets(m+2, n)

    print "Case #{}: {} {}".format(i, ans2, ans1)
    # check out .format's specification for more formatting options