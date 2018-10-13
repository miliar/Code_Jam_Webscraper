tc_num = int(input())
cases = [int(input()) for x in range(0, tc_num)]

def find_number(num):
    ns = list(str(num))
    for i in range(len(ns) - 2, -1, -1):
        if ns[i] > ns[i + 1]:
            sub = int(ns[i]) - 1
            ns[i] = str(sub)
            for j in range(i + 1, len(ns)):
                ns[j] = '9'
    return ''.join(ns)

for n, case in enumerate(cases):
    i = int(find_number(case))
    print("Case #{}: {}".format(n+1, i))

