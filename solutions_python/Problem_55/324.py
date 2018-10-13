
def roller():

    f = open('C-large.in', 'r')

    T = int(f.readline())

    for r_num in xrange(1, T+1):
        R, k, _ = map(int, f.readline().split())
        queue = map(int, f.readline().split())

        money = 0
        money_list = make_money(k, queue)

        start = money_list.pop()
        begin = money_list[:start]
        repeats = money_list[start:]

        while R and len(begin):
            money += begin.pop(0)
            R -= 1
            
        if len(repeats):
            full, rem = divmod(R, len(repeats))
            money += full * sum(repeats)
            for i in range(rem):
                money += repeats[i]

        print "Case #%d: %d" % (r_num, money)

        
        
def make_money(k, queue):
    money_list = []
    
    queues = [tuple(queue)]

    while True:
        start_queue = queue[:]
        num_in = 0

        i = 0
        while len(queue) and queue[0] + num_in <= k:
            num_in += queue.pop(0)
            i += 1

        money_list.append(num_in)
        queue += start_queue[:i]
        tup = tuple(queue)
        if tup in queues:
            money_list.append(queues.index(tup))
            break
        queues.append(tup)

    return money_list
        

        
