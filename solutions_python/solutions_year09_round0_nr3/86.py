s = 'welcome to code jam'
for case in range(input()):
    line = raw_input()
    comb = [0] * len(s)
    for j in range(len(line)):
        pos = s.find(line[j])
        while pos != -1:
            comb[pos] += 1 if pos == 0 else comb[pos - 1]
            pos = s.find(line[j], pos + 1)
    ans = str(comb[len(comb) - 1])
    ans = ans[-4:] if len(ans) >= 4 else ans.zfill(4)
    print 'Case #%s: %s' % (case + 1, ans)
