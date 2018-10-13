T = int(raw_input())
#import pudb
#pudb.set_trace()
#T = 1
#raw_input = "2 1 1 8 0"
for tc in range(T):
    inp_list = map(int, raw_input().split())
    N, S, p, ti = inp_list[0], inp_list[1], inp_list[2], inp_list[3:]
    p1 = p
    p1 = p + (p-2 ) + (p-2)
    y = 0 # result
    initial_likely_scores = []
    for each_score in ti:
        if each_score >= p1:
            divide_by_three, remainder = each_score / 3, each_score % 3
            if divide_by_three >= p:
                y += 1
                continue
            divide_equally = [divide_by_three, divide_by_three, divide_by_three]
            i = 0 # short term counter
            while remainder:
                divide_equally[i] += 1
                remainder -= 1
                i += 1
            if divide_equally[0] >= p:
                y += 1
                continue
            initial_likely_scores.append(divide_equally)

    while S and filter(None, initial_likely_scores):
        n = initial_likely_scores.pop()
        if n[0] + 1 >= p and (((n[0] + 1) - (n[1] -1)) <= 2) and (n[1]-1 >=0):
            y += 1
            S -= 1
    print 'Case #%d: %d' % (tc+1, y)

