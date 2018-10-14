import math

def match(a, b):
    # print("match: {} {} {}".format(a, b, a * 0.9 <= b <= a * 1.1))
    return a * 0.9 <= b <= a * 1.1

def match_list(aa, bb):
    # print("match_list: {} {}".format(aa, bb))
    return all(
        match(a, b) for a, b in zip(aa, bb)
    )

def rotated(original):
    return list(map(list, zip(*original)))

def solve(n, p, rs, ps):
    ps = list(map(sorted, ps))
    result = 0
    m = 1
    while len(ps[0]) > 0:
        rs_tmp = [x * m for x in rs]
        # print("rs_tmp:", rs_tmp)
        # print("ps:", ps)
        i = 0
        should_be_continue = False
        for i in range(n):
            while len(ps[i]) > 0:
                if rs_tmp[i] * 0.9 > ps[i][0]:
                    ps[i] = ps[i][1:]
                else:
                    break
            if len(ps[i]) == 0:
                return result
            if rs_tmp[i] * 1.1 < ps[i][0]:
                m += 1
                should_be_continue = True
                break
        if should_be_continue:
            continue

        if match_list(rs_tmp, [x[0] for x in ps]):
            result += 1
            ps = [x[1:] for x in ps]
        else:
            m += 1

    return result

def main():
    t = int(input())
    for i in range(t):
        n, p = list(map(int, input().split()))
        rs = list(map(int, input().split()))
        ps = []
        for y in range(n):
            ps.append(list(map(int, input().split())))
        result = solve(n, p, rs, ps)
        print("Case #{}: {}".format(i + 1, result))

if __name__ == '__main__':
    main()
