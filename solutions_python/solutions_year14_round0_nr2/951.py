import bisect

input_fname = "input.txt"
output_fname = "output.txt"
lines = [line.strip() for line in open(input_fname)]

lines_per_test = 1

def solve(inputs):
    test = [float(each) for each in inputs[0].split(' ')]
    (n_for_farm,n_extra,n_cookies) = [float(each) for each in inputs[0].split(' ')]
    cookie_per_sec = 2.0
    res = 0
    n_remaining = n_cookies - n_for_farm
    if n_remaining <= 0:
        res = n_cookies / cookie_per_sec
    else:
        while(n_remaining / cookie_per_sec > n_cookies / (cookie_per_sec + n_extra)):
            res += n_for_farm / cookie_per_sec
            cookie_per_sec += n_extra
        res += n_cookies / cookie_per_sec
    return "{0:.7f}".format(res)
def war(n_wts, k_wts):
    res = 0
    for wt in n_wts:
        index = bisect.bisect(k_wts, wt)
        if index == len(k_wts):
            k_wts.pop(0)
            res += 1
        else:
            k_wts.pop(index)
    return res

def dwar(n_wts, k_wts):
    res = 0
    for wt in n_wts:
        if wt < k_wts[0]:
            k_wts.pop()
        else:
            res += 1
            k_wts.pop(0)
    return res
    

def format_output(test_num, result):
    return "Case #" + str(test_num) + ": " + result + "\n"

fout = open(output_fname, "w")
for i in range(0,int(lines[0])):
    ans = solve(lines[i*lines_per_test+1:(i+1)*lines_per_test+1])
    fout.write(format_output(i+1,ans))
fout.close()
    
