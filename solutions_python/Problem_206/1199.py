from __future__ import division

if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t+1):
        D,N = [int(ele) for ele in raw_input().split(' ')]
        times = []
        for j in xrange(N):
        	k_j, s_j = [int(ele) for ele in raw_input().split(' ')]
        	t_j = (D-k_j)/s_j
        	times.append(t_j)
        max_time = max(times)
        speed = round(D/max_time,6)
        print('Case #{}: {}'.format(i, speed))