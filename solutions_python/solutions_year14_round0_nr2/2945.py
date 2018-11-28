f = open('in')
fo = open('out', 'w')

for T in range(int(f.readline())):
    print 'Case #%d:' % (T + 1),

    C, F, X = map(float, f.readline().strip().split(" "))
    income = float(2.0)

    time_spent = 0
    time_to_finish = float(X/income)
    time_to_farm = float(C/income)

    time_to_finish_with_farm = float(X/(income+F))

    farms = 0
    while time_to_finish > time_to_farm:
        if(time_spent + time_to_farm + time_to_finish_with_farm) < (time_spent + time_to_finish):
            # buyFarm
            time_spent += time_to_farm
            income += F

            # update values
            time_to_finish = X/income
            time_to_farm = C/income
            time_to_finish_with_farm = float(X/(income+F))
        else:
            break


    print time_spent + time_to_finish










