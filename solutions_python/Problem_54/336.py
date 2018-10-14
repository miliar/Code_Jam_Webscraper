def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a

test_cases = input()
for case_no in xrange(test_cases):
     events = [int(x) for x in raw_input().split()]
     num_elem = events.pop(0)
     events.sort()
     events.insert(0, num_elem)
     time_differences = [0]*(events[0] - 1)
     for i in xrange(events[0] - 1):
         time_differences[i] = events[i + 2] - events[i + 1]
     if(events[0] > 2):
         common_gcd = gcd(time_differences[0], time_differences[1])
         for i in xrange(events[0] - 3):
             common_gcd = gcd(common_gcd, time_differences[i + 2])
     else:
          common_gcd = time_differences[0]
     if 0 != events[1]%common_gcd:
         print 'Case #' + str(case_no + 1) + ':', common_gcd - events[1]%common_gcd
     else:
         print 'Case #' + str(case_no + 1) + ':', 0
