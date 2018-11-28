import sys
import fractions

def party_time(event_times):
    # get the GCD of the difference between the times, and figure out when the next cycle of that length will be aligned
    ntimes = len(event_times)
    differences = [abs(t1-t2) for t1 in event_times for t2 in event_times if t1!=t2]
    factor = reduce(fractions.gcd, differences)
    # in the example (26, 11, 6), differences are (15, 20, 5), GCD is 5, so get 6 to a multiple of 5
    smallest = min(event_times)
    remainder = smallest % factor
    if remainder==0: return 0
    return factor - remainder
    

infile = sys.stdin
ntests = int(infile.readline().strip())        
for i in xrange(ntests):
    t = map(long, infile.readline().strip().split())[1:]
    result = party_time(t)
    print("Case #%d: %d" % (i+1, result))