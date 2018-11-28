__author__ = 'Javier'

lines = tuple(open('B-large.in', 'r'))

f = open('output.txt', 'w')

num_inputs = int(lines[0])

for i in range(num_inputs):
    data = lines[1+i].split()
    farm_cost = float(data[0])
    farm_production = float(data[1])
    X = float(data[2])

    current_production = 2
    total_time = X / current_production
    time_buying_farms = 0

    while True:

        time_buying_farms += farm_cost / current_production
        current_production += farm_production
        time_current_production = X / current_production

        if time_buying_farms + time_current_production < total_time:
            total_time = time_buying_farms + time_current_production
        else:
            break

    print >> f, 'Case #%d: %.7f'%(i+1, total_time)

f.close()