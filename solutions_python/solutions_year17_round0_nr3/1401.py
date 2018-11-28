from Queue import PriorityQueue


f = open("3.in")
num_test = int(f.readline())

for iter_test in xrange(num_test):
    n, k = map(int, f.readline().split())
    h = PriorityQueue()
    h.put(-n)
    for i in xrange(k):
        a = -h.get()
        x = (a - 1) / 2
        y = a - 1 - x
        h.put(-x)
        h.put(-y)
    print "Case #%d:" % (iter_test + 1),
    print max(x,y), min(x,y)


