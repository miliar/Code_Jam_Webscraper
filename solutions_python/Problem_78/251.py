#!pypy
#pypy 1.5 JIT on OS X
import sys
import collections
import decimal
D = decimal.Decimal
deq = collections.deque

cases = deq(line.strip() for line in sys.stdin)
total_cases = int(cases.popleft())

for n, case in enumerate(cases, 1):
    max_today, percent_today, percent_total = map(D, case.split())
    
    # i hate myself there must be a trivial math solution...
    
    if percent_total == D("100") and percent_today != D("100"):
        result = "Broken"
    elif percent_total == D("0") and percent_today != D("0"):
        result = "Broken"
    else:
        for possible_today in range(D("1"), max_today + D("1")):
            if (percent_today / D("100") * possible_today) % D("1") == D("0"):
                result = "Possible"
                break
        else:
            result = "Broken"
    
    print "Case #%s: %s" % (n, result)
    

