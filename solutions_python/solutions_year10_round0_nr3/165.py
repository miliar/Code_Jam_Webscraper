def i(index, cycle):
    return index%cycle
test_cases = input()
for case in xrange(test_cases):
    R, K, N = [int(x) for x in raw_input().split()]
    queu = [int(x) for x in raw_input().split()]
    location = 0
    money = 0
    for ride in xrange(R):
        ride_money = 0
        start_location = location
        while start_location + N > location and queu[location%N] + ride_money <= K:
            ride_money += queu[location%N]
            location += 1
        money += ride_money
    print 'Case #' + str(case + 1) + ':', money
