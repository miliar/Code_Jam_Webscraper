from collections import deque

t = int(raw_input())



def tree_visit( begin, end):
    pointer = (end-begin)/2
    

for line in xrange(1, t + 1):
    n, k = map(int, raw_input().split())

    dq = deque([])
    begin = 0
    end = n-1

    dq.append((end-begin, begin, end))
    step = 0

    last_left = 0
    last_right = 0
    curr_range =deque([])
    nodes = 1
    while step < k:
        if len(curr_range) == 0:
            for i in range(nodes):
                if len(dq)==0:
                    break
                curr_range.append(dq.popleft())
            curr_range = deque(sorted(curr_range))
            nodes *= 2
            
        value_rank, begin, end = curr_range.popleft()

        middle_point = begin + int((end-begin) /2)
        
        left = middle_point-begin
        right = end - middle_point

        last_left = left
        last_right = right
        if right > left:
            if middle_point+1<= end:
                dq.append((n - (end-middle_point), middle_point+1, end))
            if middle_point -1 >= begin:
                dq.append((n- (middle_point-begin), begin, middle_point-1))
        elif left >= right:
            if middle_point -1 >= begin:
                dq.append((n-(end-middle_point), begin, middle_point-1))
            if middle_point+1<= end:
                dq.append((n-(middle_point-begin), middle_point+1, end))

        step += 1
        
    print "Case #{}: {} {}".format(line, max(last_left, last_right), min(last_left, last_right))
