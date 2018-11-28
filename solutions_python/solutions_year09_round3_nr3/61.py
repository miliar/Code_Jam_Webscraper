#!/usr/local/python2.5

def compute_min_coins_needed(data):
    global min_bribe_amount
    global first_time
    bribe_amount = compute_coins_needed(data)
    if (first_time or bribe_amount < min_bribe_amount):
        min_bribe_amount = bribe_amount
        first_time = False

def permute(s, data):
    for i in range(s, Q):
        data[i],data[s] = data[s],data[i]
        permute(s+1, data)
        data[i],data[s] = data[s],data[i]
    if (s+1 == Q): 
#       print data
        compute_min_coins_needed(data)

def compute_coins_needed(data):
    intervals = [[1, P]]
    bribe_amount = 0
    for prisoner_id in data:
        interval_idx = 0
        for interval in intervals:
            if (interval[0] <= prisoner_id <= interval[1]):
                bribe_amount += interval[1] - interval[0]
                left_interval = [interval[0], prisoner_id-1]
                right_interval = [prisoner_id+1, interval[1]]
                intervals[interval_idx] = left_interval
                intervals.insert(interval_idx+1, right_interval)
#               print 'prisoner', prisoner_id, 'intervals =', intervals, bribe_amount
                break
            interval_idx += 1
    return bribe_amount

T = input()
for case in xrange(T):
    (P, Q) = map(int, raw_input().split())
    release_list = map(int, raw_input().split())
    first_time = True
    permute(0, release_list)
    print 'Case #%d: %d' % (case+1, min_bribe_amount)
