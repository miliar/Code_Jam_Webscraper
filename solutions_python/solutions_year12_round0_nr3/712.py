import psyco
psyco.full()

#def generate_recycled(n, b, a, num_len):
#    s = set()
#    recycled = str(n)
#    for i in xrange(num_len):
#        recycled = recycled[-1] + recycled[0:-1]
#        if recycled[0] != '0' and a <= int(recycled, 10) <= b:
#            s.add(int(recycled, 10))
#
#    return sorted(s)

def generate_recycled(n, b, a, num_len):
    l = []
    recycled = n
    ten_power_len = 10**(num_len-1)
    for i in xrange(num_len):
        rest = recycled % 10
        recycled = recycled / 10 + rest*ten_power_len
        if rest != 0 and a <= recycled <= b:
            l.append(recycled)

    return sorted(set(l))


def generate_recycled_of_n_and_friends(n, smaller_than, bigger_than, num_len):
    recycled_of_n_and_friends = generate_recycled(n, smaller_than, bigger_than, num_len)
    #print recycled_of_n_and_friends
    d = {}
    the_len = len(recycled_of_n_and_friends) - 1
    for i, friend in enumerate(recycled_of_n_and_friends):
        d[friend] = the_len - i

    #print d
    return d


def process(s):
    import time
    start = time.time()
    a, b = map(int, s.split())
    d = {}
    result = 0
    num_len = len(str(a))
    for i in xrange(a, b+1):
        #print i
        if i not in d:
            r = generate_recycled_of_n_and_friends(i, b, a, num_len)
            d.update(r)
            result += sum(r.itervalues())

#        if i % 10000 == 0:
#            print i


    #print d
    #print time.time() - start
    return result

#print generate_recycled(13542, 99000, 10000)
#print generate_recycled_of_n_and_friends(1112, 2222, 1111)
#print process('1 9')
#print process('10 40')
#print process('100 500')
#print process('1111 2222')
#print process('1000000 2000000')

number_of_cases = int(raw_input())

for case_number in xrange(1, number_of_cases+1):
    s = raw_input()

    result = process(s)

    print "Case #%d: %s" % (case_number, result)
    case_number += 1