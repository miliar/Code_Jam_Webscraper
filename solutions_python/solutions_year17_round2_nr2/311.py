import numpy as np

def all_allowed(prev, is_last, first):
    out = []

    if is_last:
        prev = prev + first

    if 'R' not in prev:
        out.append(0)
    if 'Y' not in prev:
        out.append(1)
    if 'B' not in prev:
        out.append(2)

    return out

if __name__ == '__main__':
    t = int(raw_input())

    for i_t in np.arange(t):
        n, r, o, y, g, b, v = raw_input().split(" ")
        n = int(n)

        r = int(r)
        o = int(o)
        y = int(y)
        g = int(g)
        b = int(b)
        v = int(v)

        strings = ['R', 'Y', 'B']
        nums = np.array([r, y, b])
        nums_eff = np.array([r, y, b])
        m = n
        output = ''
        prev = ''
        first = ''
        impossible = False

        while (m > 0) and (not impossible):
            allowed = all_allowed(prev, m==1, first)
            #print allowed
            nums_allowed = nums_eff[allowed]
            if np.all(nums[allowed] == 0):
                impossible = True
                output = 'IMPOSSIBLE'
                break
            else:
                max_idx = allowed[np.argmax(nums_allowed)]
                if nums[max_idx] != 0:
                    new = strings[max_idx]
                else:
                    nums_allowed = nums[allowed]
                    max_idx = allowed[np.argmax(nums_allowed)]
                    new = strings[max_idx]

                output = output+new
                nums[max_idx] -= 1
                if m < n:
                    nums_eff[max_idx] -=1
                else:
                    first = new

                prev = new
                #print nums_allowed
            #print output
            #print nums
            #print nums_eff
            #print ""
            m -= 1

        print 'Case #%d: ' % (i_t + 1) + output