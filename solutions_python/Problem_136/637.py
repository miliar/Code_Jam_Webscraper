'''
Created on Apr 12, 2014

@author: szalivako
'''

t = int(raw_input())

for i in range(t):
    c, f, x = [float(ai) for ai in raw_input().split()]
    cur_t = 0
    min_t = 1000000000
    cur_v = 2.0

    while (True):
        if (cur_t + x / cur_v < min_t):
            min_t = cur_t + x / cur_v
        else:
            break
        cur_t += c / cur_v
        cur_v += f

    print 'Case #' + str(i + 1) + ": " + str(min_t)