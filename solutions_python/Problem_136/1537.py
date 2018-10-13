f = open("B-large.in",'r')

output = open('B-large_attempt0.out','w')

ncases = int(f.readline())

initial_rate = 2.0



for T in range(0,ncases):
    print T
    farm_cost, farm_rate, x = map(float, f.readline().split())

    current_rate = initial_rate
    farm_purchase_times = [0]
    farming_complete_times = [x/current_rate]

    farm_purchase_times.append(farm_purchase_times[-1] + farm_cost / current_rate)
    current_rate += farm_rate
    farming_complete_times.append(farm_purchase_times[-1] + x / current_rate)

    while farming_complete_times[-1] < farming_complete_times[-2]:
        farm_purchase_times.append(farm_purchase_times[-1] + farm_cost / current_rate)
        current_rate += farm_rate
        farming_complete_times.append(farm_purchase_times[-1] + x / current_rate)


    output.write('Case #'+str(T+1)+': %.7f'%farming_complete_times[-2]+'\n')

output.close()
        
    
