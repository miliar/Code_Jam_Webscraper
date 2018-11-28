def check_cases(n, k):
    if n == k:
        print('Case #' + str(i+1) + ': 0 0')
        return
    last = n
    lst = []
    ls = -1
    rs = -1
    for j in xrange(0, k):
        if last > 0:
            if len(lst) > 0:
                lst.remove(last)
                if last%2 == 0:
                    lst.append(int(last/2))
                    lst.append(int((last/2)-1))
                    ls = int(last/2)
                    rs = int((last/2)-1)
                else:
                    last = last - 1
                    lst.append(int(last/2))
                    lst.append(int(last/2))
                    ls = int(last/2)
                    rs = int(last/2)
            else:
                if last%2 == 0:
                    lst.append(int(last/2))
                    lst.append(int((last/2)-1))
                    ls = int(last/2)
                    rs = int((last/2)-1)
                else:
                    last = last - 1
                    lst.append(int(last/2))
                    lst.append(int(last/2))
                    ls = int(last/2)
                    rs = int(last/2)
            last = max(lst)
    print('Case #' + str(i+1) + ': ' + str(ls)) + ' ' + str(rs)



test_cases = int(raw_input())
for  i in xrange(0, test_cases):
    input_t = raw_input().split()
    n = int(input_t[0])
    k = int(input_t[1])
    check_cases(n, k)
    