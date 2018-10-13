def get_untidy_index(s):
    s = str(s)
    highest = 0
    for i in range(len(s)):
        if int(s[i]) < highest:
            return i
        highest = max(int(s[i]), highest)
    return -1
    
def get_highest_tidy(N):
    current = N
    index = get_untidy_index(current)
    while index != -1:
        next_str = ""
        current_str = str(N)
        for i in range(len(current_str)):
            if i == index - 1:
                next_str += str(int(current_str[i])-1)
            elif i >= index:
                next_str += '9'
            else:
                next_str += current_str[i]
        current = int(next_str)
        index = get_untidy_index(current)
    return int(current)
    
def parse_input():
    T = int(raw_input())
    for i in range(1, T+1):
        N = int(raw_input())
        print "Case #{0}: {1}".format(str(i), str(get_highest_tidy(N)))

parse_input()
