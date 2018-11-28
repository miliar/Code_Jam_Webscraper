
T = int(raw_input().strip())

for idx in range(1, T+1):
    N, K = map(int, raw_input().split())

    stalls = [0 for i in range(N+2)]
    stalls[0] = 1
    stalls[N+1] = 1

    SL = -1
    SR = -1
    # find biggest gaps from left
    for p in range(K):
        num = 1
        SL = -1
        SR = -1
        max_gaps = -1
        old_selected = -1
        selected = -1
        while num < len(stalls):
            if stalls[num] == 1:
                num += 1
                continue

            gap_start = num
            gap_end = num
            while num < len(stalls) and stalls[num] != 1:
                if stalls[num] == 0:
                    gap_end = num
                num += 1

            gaps = gap_end - gap_start
            if max_gaps < gaps:
                max_gaps = gaps
                selected = gap_start + (gaps/2)
                SL = selected - gap_start
                SR = gap_end - selected
                #print "start", gap_start, "end",gap_end, "selected", selected
                stalls[selected] = 1
                if old_selected != -1:
                    stalls[old_selected] = 0
                old_selected = selected

        #print stalls

    print "Case #%d: %d %d" % (idx, max(SL, SR), min(SL, SR))


