def is_tidy(candidate):
    is_tidy = True
    str_candidate = str(candidate)
    current_max_digit = str_candidate[0]
    for i in xrange(1, len(str_candidate)):
        if str_candidate[i] < current_max_digit:
            is_tidy = False
            break
        current_max_digit = str_candidate[i]
    return is_tidy

def get_candidate_tidy_num(n):
    #print n
    str_n = str(n)
    length = len(str_n)
    longest_increasing_run = 1
    current_max_digit = str_n[0]
    for i in xrange(1, length):
        if str_n[i] >= current_max_digit:
            current_max_digit = str_n[i]
            longest_increasing_run += 1
        else:
            break
    #print longest_increasing_run
    candidate = int(str_n[0:longest_increasing_run])
    if candidate < n:
        candidate -= 1
    #print candidate
    while candidate < n:
        tmp = candidate * 10 + 9
        if tmp > n:
            break
        else:
            candidate = tmp
    # check if it is tidy
    while not is_tidy(candidate):
        candidate = get_candidate_tidy_num(candidate)
    return candidate

with open("tidy_numbers.large", 'r') as f:
    lines = f.read().strip().split('\n')
    testcases = int(lines[0])
    for case in xrange(1, testcases + 1):
        n = int(lines[case])
        candidate = get_candidate_tidy_num(n)
        print("Case #%s: %s" % (str(case), str(candidate)))
