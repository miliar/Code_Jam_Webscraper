
def istidynum(input_num):
    result = True
    now = int(str(input_num)[0])
    for i in str(input_num)[1:]:
        #print now, " ", i
        if int(i) >= now:
            now = int(i)
        else:
            result = False
            break
    return result

def tidynum(input_num):
    result = input_num
    while True:
        if istidynum(result):
            break
        else:
            result = result - 1
    return result

test_input = int(raw_input())
for case in xrange(1, test_input+1):
    input_num = int(raw_input())
    print "Case #{}: {}".format(case, tidynum(input_num))