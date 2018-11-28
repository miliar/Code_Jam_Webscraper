def read_int_line(f):
    return int(f.readline().replace("\n",""))

def read_int_arr(f):
    return map(int, f.readline().replace("\n","").split(" "))

def gcd(a, b):
    while b:
        t = b
        b, a = a % b, t
    return a

def gcd_nums(nums):
    a = nums.next()
    try:
        b = nums.next()
    except StopIteration:
        return a
    _gcd = gcd(a, b)
    for num in nums:
        _gcd = gcd(_gcd, num)
    return _gcd

def main(inf, outf):
    fr = open(inf)
    fw = open(outf, 'w')
    T = read_int_line(fr)
    for i in range(T):
        events = read_int_arr(fr)[1:]
        if i % 100 == 0:
            print i
        res = "Case #%d: %d\n" % (i+1, result(events))
        fw.write(res)
    fw.close()
    fr.close()

def diffs(events):
    dif = events[0] - events[1]
    yield abs(dif)
    event_before = events[1]
    for event in events[2:]:
        dif = event_before - event
        event_before = event
        yield abs(dif)

def result(events):
    g = gcd_nums(diffs(events))
    m = min(events)
    if m % g == 0:
        return 0
    d = abs(m - ((m / g + 1) * g))
    return d

if __name__ == "__main__":
    main("B-large.in", "warning.out")
#    print gcd_nums(diffs([90001,80001]))
#    import random
#    aa = []
#    for k in range(100):
#        aa.append([random.randint(10**49, 10**50) for i in range(1000)])
#
#    print "Counting"
#    for a in aa:
#        gcd_nums(a)

#    import psyco
#    psyco.full()
#    import timeit
#    s ="gcd2(13245678901324567890132456789013245678901324567890, 987654321065498732109876543210654987321012345000)"
#    t = timeit.Timer(stmt=s,setup="from __main__ import gcd2")
#    print "%.10f usec/pass" % (1000000 * t.timeit(number=10000000)/1000000)