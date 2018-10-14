import operator
from Queue import PriorityQueue

fin = open('B.in', 'r')
fout = open('B_3.out', 'w')

ind2str = {0: 'R', 1: 'O', 2: 'Y', 3: 'G', 4: 'B', 5: 'V'}

T = int(fin.readline())
for t in range(1, T+1):
    pq = PriorityQueue()
    arr = map(int, fin.readline().split())
    N = arr[0]
    unicorns = arr[1:]
    # priority queue of (-(num of color), ind of color)
    for i, elt in enumerate(unicorns):
        if elt != 0:
            pq.put((-elt, i))
    max_uni, prev = pq.get()
    # check if max is greater than sum of rest
    if -max_uni > sum(unicorns) + max_uni:
        fout.write('Case #' + str(t) + ': IMPOSSIBLE\n')
        continue
    ans = ind2str[prev]
    first = prev
    pq.put((max_uni + 1, prev))
    N -= 1
    while N > 0:
        hold_off = []  # list of elements to pop on queue later
        assert not pq.empty()
        neg_num, i = pq.get()
        #print (pq.queue)
        # get the next best candidate
        if (N == 1 and i == first):
            assert ind2str[i] != ans[-2]
            switch = ans[-1]
            ans = ans[:-1]
            ans += ind2str[i]
            ans += switch
            break;
        if i == prev: #or (N == 1 and i == first):
            hold_off.append((neg_num, i))
            assert not pq.empty()
            neg_num, i = pq.get()
        # add element to string, update prev, and +1 to neg_num
        ans += ind2str[i]
        N -= 1
        prev = i
        new_num = neg_num + 1
        if new_num != 0:
            hold_off.append((new_num, i))
        # add back elements we took out
        for elt in hold_off:
            pq.put(elt)
    fout.write('Case #' + str(t) + ': {}\n'.format(ans))
