import sys
import re


def solve(empty_stall_count, people):
    if empty_stall_count == people:
        return "0 0"
    row = ["1"] + ["0"] * empty_stall_count + ["1"]
    data = ["", "", ""]
    for p in range(1, people + 1):
        data = find_stall(row)
        row[data[0]] = "1"
        # print (''.join(row))
    return str(data[1]) + " " + str(data[2])


def find_stall(row):
    str_row = ''.join(row)
    matches = re.findall('0+', str_row)
    longest = max(matches)
    m = re.search(longest, str_row)

    empty = m.end() - m.start();
    # print(str_row)
    # print("start:" + str(m.start()) + " end:" + str(m.end()));
    if empty == 1:
        center = m.start()
        max_lr = 0
        min_lr = 0
    elif empty == 2:
        center = m.start()
        max_lr = 1
        min_lr = 0
    else:
        center = m.start() + int((m.end() - m.start()) / 2)
        if (m.end() - m.start()) % 2 == 0:
            center -= 1
        l = center - m.start()
        r = m.end() - center - 1
        # print("l:" + str(l) + " r:" + str(r))
        max_lr = max(l, r)
        min_lr = min(l, r)

    # print ("center:" + str(center) + " max:" + str(max_lr) + " min:" + str(min_lr))
    return [center, max_lr, min_lr]


if __name__ == "__main__":
    import fileinput

    f = fileinput.input()
    T = int(f.readline())
    for case in range(1, T + 1):
        line = f.readline().strip().split(" ")
        empty_stall_count = int(line[0]);
        people = int(line[1]);
        r = solve(empty_stall_count, people)
        print("Case #{0}: {1}".format(case, r))
