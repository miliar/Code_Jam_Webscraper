case_am = int(input())
for case in range(1, case_am + 1):
    am_needed = 0
    cur_level = 0
    max_s, levels = input().split()
    max_s = int(max_s)
    for level in range(max_s + 1):
        if level <= cur_level:
            cur_level += int(levels[level])
        else:
            am_needed += (level - cur_level)
            cur_level += (level - cur_level) + int(levels[level])
    print("Case #", case, ": ", am_needed, sep="")