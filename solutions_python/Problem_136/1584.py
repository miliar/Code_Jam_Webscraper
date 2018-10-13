import sys

def do_test_case(fd):
    tokens = fd.readline().split();

    factory_cost = float(tokens[0])
    factory_out = float(tokens[1])
    cookie_goal = float(tokens[2])
    
    factories = 0
    last_cost = 0

    while True:
        denom = (factories*factory_out+2)
        next_denom = ((factories+1)*factory_out+2)

        w_fac = last_cost + factory_cost/denom + cookie_goal/next_denom
        w_out = last_cost + cookie_goal/denom

        if w_out <= w_fac:
            return w_out
        else:
            last_cost += factory_cost/denom
            factories += 1


##################
file = sys.argv[1]

fd = open(file, 'r')

num_tests = fd.readline()

for i in xrange(1,int(num_tests)+1):
    print "Case #%d: %f" % (i,do_test_case(fd))

