def main():
    # read in number of samples
    N = int(raw_input().strip())

    for c in xrange(N):
        T = int(raw_input().strip())
        NA, NB = raw_input().split()
        NA = int(NA)
        NB = int(NB)

        a_q = []
        b_q = []

        # read data for a
        for i in xrange(NA):
            data        = raw_input()
            s, e        = data.split()
            s_h, s_m    = s.split(':')
            e_h, e_m    = e.split(':')

            s_h         = int(s_h)
            s_m         = int(s_m)
            s_t         = s_h * 60 + s_m

            e_h         = int(e_h)
            e_m         = int(e_m)
            e_t         = e_h * 60 + e_m + T

            a_q.append((s_t, 'D'))
            b_q.append((e_t, 'A'))

        # read data for b
        for i in xrange(NB):
            data        = raw_input()
            s, e        = data.split()
            s_h, s_m    = s.split(':')
            e_h, e_m    = e.split(':')

            s_h         = int(s_h)
            s_m         = int(s_m)
            s_t         = s_h * 60 + s_m

            e_h         = int(e_h)
            e_m         = int(e_m)
            e_t         = e_h * 60 + e_m + T

            b_q.append((s_t, 'D'))
            a_q.append((e_t, 'A'))

        a_q.sort()
        b_q.sort()

        cur_a  = 0
        need_a = 0

        for t, action in a_q:
            if action == 'D':
                if cur_a > 0:
                    cur_a -= 1
                else:
                    need_a += 1
            elif action == 'A':
                cur_a += 1

        cur_b  = 0
        need_b = 0

        for t, action in b_q:
            if action == 'D':
                if cur_b > 0:
                    cur_b -= 1
                else:
                    need_b += 1
            elif action == 'A':
                cur_b += 1
        print 'Case #%d: %d %d' % (c + 1, need_a, need_b)

main()
