from sys import stdin

N = int(stdin.readline())
for case_index in xrange(1, N+1):

    line = stdin.readline().strip().split(' ')
    C,F,X = float(line[0]),float(line[1]),float(line[2])

    prod_rate = 2
    time = 0.0
    another_farm = True

    while another_farm:
        time = time + (C / prod_rate)
        next_prod_rate = prod_rate + F

        prod_all_time = (X - C) / prod_rate
        prod_next_time = X / next_prod_rate

        if ( prod_all_time < prod_next_time ):
            time = time + prod_all_time
            another_farm = False

        prod_rate = next_prod_rate

    print "Case #" + str(case_index) + ": " + str(time)

