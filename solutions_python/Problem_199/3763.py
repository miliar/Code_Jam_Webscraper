def flip(ss, beg, n):
    for i in range(beg, beg + n):
        ss[i] = not ss[i]


def foo(ss, n):
    cnt = 0
    for i in range(len(ss) - n + 1):
        if not ss[i]:
            flip(ss, i, n)
            cnt += 1
            # print(cnt, ss)
        else:
            continue
    if min(ss):
        return (str(cnt))
    else:
        return ("IMPOSSIBLE")


def main_solve():
    line_in = input().split()
    ss = str(line_in[0])
    ss = [s == '+' for s in ss]
    n = int(line_in[1])
    return foo(ss, n)


num = int(input())
for _ in range(num):
    print("CASE #{0}: ".format(_ + 1) + main_solve())
