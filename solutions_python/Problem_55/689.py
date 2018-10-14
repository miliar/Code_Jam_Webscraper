test_cases = int(raw_input())
case = 1

while test_cases > 0:
    # R, k and N
    num_rides, max_ppl, num_groups = map(int, raw_input().rstrip().split())
    # N space separated groups
    groups = map(int, raw_input().rstrip().split())
    ride_counter = 1
    earnings = 0
    while ride_counter <= num_rides:
        # keep adding people till capacity is reached
        cur_ppl = 0
        index = 0
        for each in groups:
            if cur_ppl < max_ppl and cur_ppl+each <= max_ppl:
                cur_ppl += each
                index += 1
            else:
                g2 = groups[:index]
                g1 = groups[index:]
                groups = g1 + g2
                break
        earnings += cur_ppl
        ride_counter += 1
    print "Case #%d: %d" %(case, earnings)
    case += 1
    test_cases -= 1
