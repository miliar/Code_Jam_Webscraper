import sys

def get_line():
    return sys.stdin.readline().strip()

def read_nums():
    return [int(item) for item in get_line().split(" ")]

exp_multi_memo = {}
def expect_multi_group( count ):
    global exp_multi_memo
    if count <= 1:
        return 0.0
    if count in exp_multi_memo:
        return exp_multi_memo[count]
    res = 0.0
    for i in range(1, count+1):
        res += expect_group(i) + expect_multi_group(count - i)
    res /= count
    exp_multi_memo[count] = res
    return res

exp_memo = {}
def expect_group( count ):
    global exp_memo
    if count <= 1:
        return 0.0
    if count in exp_memo:
        return exp_memo[count]
    res = 0.0
    for i in range(1, count):
        res += 1.0 + expect_group(i) + expect_multi_group(count - i)
    res = (1.0 + res) / (count - 1)
    exp_memo[count] = res
    return res

def solve( array ):
    res = 0.0
    checked = [0] * len(array)
    for i in range(len(array)):
        if checked[i]:
            continue
        j = i
        count = 1
        while(array[j] != i+1):
            j = array[j]-1
            checked[j] = 1
            count += 1
            continue
        res += expect_group(count)
    
    return res

(T,) = read_nums()
for test in range(1, T+1):
    (N,) = read_nums()
    array = read_nums()
    res = solve( array )
    print "Case #%d: %f" % (test, res)

