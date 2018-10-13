T = int(input())
for case in range(T):
    invited_friend = 0
    actual_clapping = 0
    (s_max, input_line) = input().split(' ')
    s_max = int(s_max)
    i = 0
    for c in input_line:
        actual_clapping += int(c)
        new_invited = max(0, i - actual_clapping + 1)
        invited_friend += new_invited
        actual_clapping += new_invited
        if s_max <= actual_clapping:
            break
        i += 1
    print("Case #%d: %d" % (case + 1, invited_friend))
