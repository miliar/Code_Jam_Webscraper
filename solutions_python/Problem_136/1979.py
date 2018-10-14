input_file = open("B-large.in")

num_t = int(input_file.readline())

for t in xrange(num_t):
    line = input_file.readline()
    
    (c, f, x) = (float(s) for s in line.split(' '))

    current_f = 2
    
    total_time = 0

    while (False == False):
        first_way = x / current_f

        lol_i_should_buy_a_factory = c / current_f

        second_way = lol_i_should_buy_a_factory + x / (current_f + f)

        if (first_way < second_way):
            total_time += first_way
            break
        else:
            total_time += lol_i_should_buy_a_factory
            current_f += f

    print 'Case #' + str(t + 1) + ': ' + str(total_time)