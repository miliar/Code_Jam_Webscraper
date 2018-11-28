my_file = open('q2file.in' , 'r')
amount = int(my_file.readline())

def print_result(caseno , time_needed):
    print "Case #" + str(caseno) + ": %.7f" % (time_needed)


for i in xrange(0,amount):
    current = str(my_file.readline()).split()
    # Farm price
    c = float(current[0])
    # Farm speed
    f = float(current[1])
    # Amount needed
    x = float(current[2])
    
    speed = 2
    time_spent = 0
    done = False
    while not done:
        without_farm = x/speed
        with_farm = c/speed + x/(speed+f)
        if without_farm <= with_farm:
            print_result(i+1 , without_farm + time_spent)
            done = True
        # Buying farm
        else:
            time_spent += c/speed
            speed += f
            
