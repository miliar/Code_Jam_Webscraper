
def cnt_recycled(lower, upper):
    if upper < 10:
        return 0
    if lower < 10:
        lower = 10
    open_list = range(lower, upper+1)
    closed_list = set()
    count = 0

    # generate recycled no's for each entry in open_list
    for i in open_list:
        ss = str(i)
        s = str(i)
        max_len = len(s)
        max_iter = max_len
        closed_list.add(ss + "," + s)
        while max_iter > 1:
            if s[-1] == '0':
                k = max_len-1
                while s[k] == '0' and k >= 0:
                    k -= 1
                max_iter -= (max_iter-1-k)
                s = s[k:] + s[:k]
                continue
            else:
                s = s[-1:] + s[:-1]
                if (ss + "," + s) not in closed_list:
                    closed_list.add(ss + "," + s)
                    closed_list.add(s + "," + ss)
                    k = int(s)
                    if k <= upper and k >= lower:
                        count += 1
            max_iter -= 1
    return count

if __name__ == "__main__":
    input()
    try:
        case_cnt = 1
        while True:
            (lower, upper) = input().split()
            lower = int(lower)
            upper = int(upper)
            print("Case #{0}: {1}".format(case_cnt, cnt_recycled(lower, upper)))
            case_cnt += 1
    except:
        pass
