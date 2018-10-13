from collections import defaultdict, Counter
tt = int(raw_input())
for c in xrange(1, tt+1):
    num_seats, num_customer, num_tickets = map(int, raw_input().split())
    all_tickets = [map(int, raw_input().split()) for _ in xrange(num_tickets)]
    tickets_by_seat = defaultdict(list)
    for t in all_tickets:
        seat, customer = t
        tickets_by_seat[seat].append(customer)
    
    height = 0
    filled = 0
    used = Counter()
    promotions = []
    
    # print tickets_by_seat

    for seat in xrange(1, num_seats+1):
        customers = tickets_by_seat[seat]
        prev_filled = filled
        filled += len(customers)
        cc = Counter(customers)
        
        
        #print height, filled
        height = max(height, (filled+seat-1)//seat)
        height = max(height, max(cc.values() or [0]))
        space = (seat-1) * height - prev_filled # check this?
        #print height
        
        can_promote = 0
        for customer, count in cc.iteritems():
            can_promote += min(space, height - used[customer])
        
        if height > len(customers):
            should_promote = 0
        else:
            should_promote = min(can_promote, len(customers) - height, space)
        promotions.append([should_promote, len(customers), height])
        
        used.update(cc)
        height = max(height, len(customers) - should_promote, max(used.values() or [0]))

        
        #print seat, space, customers, filled, can_promote, should_promote, height
        # print used
    
    num_promotions = 0
    for p in promotions:
        effect, upper, lower = p
        if upper < height:
            continue
        num_promotions += min(upper-height, effect)
        
    print("Case #{}: {} {}".format(c, height, num_promotions))
    