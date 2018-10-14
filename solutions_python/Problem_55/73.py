def main():
    T = int(raw_input())
    for i in range(T):
        # input & init
        RkN = raw_input().split(' ')
        R = int(RkN[0])
        k = int(RkN[1])
        N = int(RkN[2])
        g = [int(g_i) for g_i in raw_input().split(' ')]
        visited = [False] * N
        # go over until revisit
        round = 0
        earn = 0
        curr = 0
        while not visited[curr] and round < R:
            visited[curr] = True
            begin = curr
            space = k
            while space >= g[curr]:
                space -= g[curr]
                curr = (curr + 1) % N
                if curr == begin:
                    break
            earn += k - space
            round += 1
        if round == R:
            print "Case #%d: %d" % (i + 1, earn)
            continue
        # found the head of the loop
        head = curr
        pre_loop_round = 0
        pre_loop_earn = 0
        curr = 0
        while curr != head:
            begin = curr
            space = k
            while space >= g[curr]:
                space -= g[curr]
                curr = (curr + 1) % N
                if curr == begin:
                    break
            pre_loop_earn += k - space
            pre_loop_round += 1
        # got details of the loop
        loop_round = round - pre_loop_round
        loop_earn = earn - pre_loop_earn
        res_before_tail = pre_loop_earn \
            + (R - pre_loop_round) / loop_round * loop_earn
        tail_round = (R - pre_loop_round) % loop_round
        tail_earn = 0
        curr = head
        remain_round = tail_round
        while remain_round > 0:
            begin = curr
            space = k
            while space >= g[curr]:
                space -= g[curr]
                curr = (curr + 1) % N
                if curr == begin:
                    break
            tail_earn += k - space
            remain_round -= 1
        print "Case #%d: %d" % (i+ 1, res_before_tail + tail_earn)
    
if __name__ == "__main__":
    main()
    