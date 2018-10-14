from decimal import Decimal
results = []

num_of_cases = int(raw_input())
for case_num in xrange(num_of_cases):
    print case_num
    timer = Decimal(0.0)
    amount = Decimal(0.0)
    cookie_count = Decimal(2.0)
    c, f, x = [Decimal(x) for x in raw_input().split()]
    while True:
        diff_to_farm = c - amount
        
        diff = x - diff_to_farm
        diff_after_buy = diff + c
        
        time_with_new_farm = diff_after_buy / (cookie_count + f)
        time_without_new_farm = diff / cookie_count
        
        if time_with_new_farm < time_without_new_farm:
            timer += diff_to_farm / cookie_count
            cookie_count += f
        else:
            timer += time_without_new_farm
            timer += diff_to_farm / cookie_count
            break

    results.append(timer)
        
        
# Print results
for ind, res in enumerate(results):
    print 'Case #%d: %0.7f' % (ind + 1, res)
