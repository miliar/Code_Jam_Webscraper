
number_of_tests = int(raw_input())

def rotate(l):
    last = l[-1]
    i = len(l) - 1
    while i > 0:
        l[i] = l[i - 1]
        i -= 1
    l[0] = last

def count_recycled_pairs():
    a, b = raw_input().split()
    rotations_to_do = len(a) - 1
    a, b = int(a), int(b)

    done = set()

    for n in xrange(a, b):
        m_deq = list(str(n))

        i = 0
        while i < rotations_to_do:
            i += 1

            rotate(m_deq)
            if m_deq[0] == '0':
                continue

            m = int(''.join(m_deq))

            if n < m <= b:
                done.add((n, m))

    return len(done)


for test in xrange(number_of_tests):
    print "Case #%s: %s" % (test + 1, count_recycled_pairs())

