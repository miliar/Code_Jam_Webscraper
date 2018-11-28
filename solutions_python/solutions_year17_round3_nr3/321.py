import numpy as np

if __name__ == '__main__':
    t = int(raw_input())

    for t_i in np.arange(t):
        n, k = raw_input().split(" ")
        u = raw_input()
        p_list = raw_input().split(" ")
        n = int(n) # number cores
        k = int(k) # number cores function properly
        u = float(u)

        p_list = [float(p) for p in p_list]
        p_list = sorted(p_list)
        # print p_list

        u_remain = u
        for i in np.arange(n):
            if i < n-1:
                diff = p_list[i+1] - p_list[i]
                if u_remain >= (i+1)*diff:
                    for j in np.arange(i+1):
                        p_list[j] += diff
                    u_remain -= (i+1)*diff
                else:
                    for j in np.arange(i + 1):
                        p_list[j] += u_remain/float(i+1)
                    u_remain = 0.
            else:
                for j in np.arange(i + 1):
                    p_list[j] += u_remain / float(i + 1)

        prod = 1.
        for p in p_list:
            prod *= p

        # print u
        # print p_list

        print 'Case #%d: ' % (t_i + 1) + '%1.8f' % prod