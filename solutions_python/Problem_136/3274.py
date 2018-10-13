import sys

N = input()

for i in xrange(N):
    line = raw_input()
    farm_cost, farm_rate, quota = map(float, line.split(' '))

    time = 0.0
    rate = 2.0

    while True:
        if farm_cost / rate + quota / (rate + farm_rate) <= quota / rate:
            # buy a farm
            time += farm_cost / rate
            rate += farm_rate
        else:
            # wait until quota is reached
            time += quota / rate
            break
    print 'Case #{num}: {time}'.format(num=i+1,time=time)
