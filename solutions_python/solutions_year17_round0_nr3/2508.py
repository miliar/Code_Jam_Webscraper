import sys


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):

        n, k = map(int, raw_input().split(" "))

        stalls = [False for _ in range(n+2)]
        stalls[0] = True
        stalls[-1] = True

        # initialize
        values = []
        for j in range(len(stalls)):
            if stalls[j]:
                # this stall is occupied
                values.append(None)
                continue

            l_s = 0
            for m in reversed(range(0, j)):
                if stalls[m]:
                    break
                l_s += 1
            r_s = 0
            for m in range(j+1, n+2):
                if stalls[m]:
                    break
                r_s += 1
            values.append([l_s, r_s])

        for p in range(k):
            min_vals_max = -1
            for j, values_i in enumerate(values):
                if values_i:
                    min_val = min(values_i)
                    if min_val > min_vals_max:
                        min_vals_max = min_val
                        min_vals_max_ids = []
                    if min_val == min_vals_max:
                        min_vals_max_ids.append(j)

            chosen_stall = None
            if len(min_vals_max_ids) == 1:
                chosen_stall = min_vals_max_ids[0]
            else:
                max_vals_max = -1
                for j in min_vals_max_ids:
                    max_val = max(values[j])
                    if max_val > max_vals_max:
                        max_vals_max = max_val
                        max_vals_max_ids = []
                    if max_val == max_vals_max:
                        max_vals_max_ids.append(j)

                if len(max_vals_max_ids) == 1:
                    chosen_stall = max_vals_max_ids[0]
                else:
                    chosen_stall = sorted(max_vals_max_ids)[0]

            stalls[chosen_stall] = True
            max_val = values[chosen_stall][1]
            min_val = values[chosen_stall][0]
            values[chosen_stall] = None
            # update stalls between occupied - chosen & chosen - occupied
            for j in reversed(range(chosen_stall)):
                if stalls[j]:
                    break
                values[j][1] = chosen_stall - j - 1
            for j in range(chosen_stall + 1, len(stalls)):
                if stalls[j]:
                    break
                values[j][0] = j - chosen_stall - 1

        print "Case #%d: %d %d" % (i, max_val, min_val)
