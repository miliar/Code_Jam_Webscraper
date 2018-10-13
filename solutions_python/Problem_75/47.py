import sys

def get_line():
    return sys.stdin.readline().strip()

def read_nums():
    return [int(item) for item in get_line().split(" ")]

def solve(comb_dic, opposed_set, elements):
    res = []
    for elem in elements:
        if len(res) <= 0:
            res.append(elem)
            continue
        prev = res[-1]
        if prev+elem in comb_dic:
            res.pop()
            res.append(comb_dic[prev+elem])
            continue
        flag = False
        for one in res:
            if one+elem in opposed_set:
                flag = True
                break
        if flag:
            res = []
            continue
        res.append(elem)
    return res

(T,) = read_nums()
for test in range(1, T+1):
    test_case = get_line().split(" ")
    C = int(test_case.pop(0))
    comb_dic = {}
    for i in range(C):
        str = test_case.pop(0)
        comb_dic[str[0]+str[1]] = str[2]
        comb_dic[str[1]+str[0]] = str[2]
    D = int(test_case.pop(0))
    opposed_set = set()
    for i in range(D):
        str = test_case.pop(0)
        opposed_set.add(str[0]+str[1])
        opposed_set.add(str[1]+str[0])
    N = int(test_case.pop(0))
    elements = list(test_case.pop(0))
    res = solve(comb_dic, opposed_set, elements)

    print "Case #%d: [%s]" % (test, ", ".join(res))

