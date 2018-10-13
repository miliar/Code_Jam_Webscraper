import sys

debug_stage = True
cache_item = {"c_upper_lim":0,"c_tidy_num":-1}

def debug_print(inp):
    if debug_stage == True:
        print(inp)


def int_ToArray(num):

    num_string = str(num)
    out = []
    for d in num_string:
        out.append(int(d))
    return out;

def isTidy(int_inp):
    num_Arr = int_ToArray(int_inp)
    arr_len = len(num_Arr)

    if arr_len == 1: # < 10 is tidy
        return True
    for ind in range(arr_len-1):

        if num_Arr[ind] > num_Arr[ind + 1]:
            return False
    return True


def get_last_tidy(upper_lim):
    out = -1
    real_lower_lim = 1
    for i in range(real_lower_lim,upper_lim+1): # includes N 7
        debug_print(i)
        if isTidy(i):
            out = i
            debug_print("new tidy found: %d"%i)
    return out


open_name = sys.argv[1]
debug_print(open_name)
f = open(open_name, 'r')
out_f = open('out.txt', 'w')


my_line = f.readline()
num_of_tests = int(my_line)
debug_print(num_of_tests)
for c in range(1, num_of_tests + 1):
    debug_print("working on case #%d" % (c))
    my_line = f.readline()
    upp_lim = int(my_line) # N include this to search
    res_out = get_last_tidy(upp_lim)
    if res_out == -1:
        out_f.write("Case #%d: IMPOSSIBLE\n" % (c))
    else:
        out_f.write("Case #%d: %d\n" % (c, res_out))


    out_f.flush()

out_f.close()
