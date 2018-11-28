# -*- coding: utf-8 -*-
t = int(raw_input())
for case_nr in xrange(1, t + 1):
    n = int(raw_input())
    s = ""
    s_a = []
    flag = True
    for i in xrange(0, n):
        t_s = raw_input()
        s_a.append([])
        ans_s = ""
        t_i = 1
        for j in xrange(0, len(t_s) - 1):
            if t_s[j] != t_s[j + 1]:
                ans_s += t_s[j]
                s_a[i].append(t_i)
                t_i = 1
            else:
                t_i += 1
        ans_s += t_s[len(t_s) - 1]
        s_a[i].append(t_i)
        if s == "":
            s = ans_s
        elif s != ans_s:
            print "Case #%d: Fegla Won" % case_nr
            flag = False
            break
    if not flag:
        continue
    t_ans = 0
    for i in xrange(0, len(s)):
        t_sum = 0
        for j in xrange(0, n):
            t_sum += s_a[j][i]
        t_sum = round(t_sum * 1.0 / n)
        for j in xrange(0, n):
            t_ans += abs(s_a[j][i] - t_sum)
    print "case #%d: %d" % (case_nr, int(t_ans))
