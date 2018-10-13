import numpy as np

def shortest_time(i, n, e_curr, s_curr, e_list, s_list, D):
    if i == (n-2):
        # stop recursion
        if e_curr >= D[i, i+1]:
            t_curr = float(D[i, i+1])/float(s_curr)
        else:
            t_curr = 1.e12

        if e_list[i] >= D[i, i+1]:
            t_new = float(D[i, i+1])/float(s_list[i])
        else:
            t_new = 1.e12
        return min(t_curr, t_new)

    else:
        if (e_curr >= D[i, i + 1]) and (e_list[i] < D[i, i+1]):
            t_curr = float(D[i, i + 1]) / float(s_curr)
            return t_curr + shortest_time(i+1, n, e_curr-D[i, i+1], s_curr, e_list, s_list, D)
        elif (e_curr < D[i, i + 1]) and (e_list[i] >= D[i, i+1]):
            t_new = float(D[i, i + 1]) / float(s_list[i])
            return t_new + shortest_time(i+1, n, e_list[i]-D[i, i+1], s_list[i], e_list, s_list, D)
        else:
            t_curr = float(D[i, i + 1]) / float(s_curr)
            t_new = float(D[i, i + 1]) / float(s_list[i])
            return min(t_curr + shortest_time(i+1, n, e_curr-D[i, i+1], s_curr, e_list, s_list, D),
                       t_new + shortest_time(i + 1, n, e_list[i] - D[i, i + 1], s_list[i], e_list, s_list, D))

if __name__ == '__main__':
    t = int(raw_input())

    for t_i in np.arange(t):
        n, q = raw_input().split(" ")
        q = int(q)
        n = int(n)

        e_list = []
        s_list = []
        for i_n in np.arange(n):
            e, s = raw_input().split(" ")
            e_list.append(int(e))
            s_list.append(int(s))

        D = np.empty((n, n))
        for i_n in np.arange(n):
            d = np.array(raw_input().split(" "))
            D[i_n, :] = d

        u_list = []
        v_list = []
        for i_q in np.arange(q):
            u, v = raw_input().split(" ")
            u_list.append(int(u))
            v_list.append(int(v))

        #print e_list
        #print s_list
        #print D

        output = shortest_time(0, n, e_list[0], s_list[0], e_list, s_list, D)

        print 'Case #%d: ' % (t_i + 1) + str(output)