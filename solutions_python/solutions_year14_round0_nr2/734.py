#read off input, 

infile = open("B-large.in", 'r')
op_file = open('output.txt', 'w+')


num_cases = int(infile.readline())

start_rate = 2.0

for case_num in range(num_cases):

    farm_cost, farm_rate, target = [float(k) for k in ((infile.readline()).split())]
    farms = 0.0
    farm_time = 0.0
    time = target/start_rate

    def time_req(farm, farm_time): return farm_time + target/(farm*farm_rate + start_rate)
    def farms_time(current_time, farm): return current_time+farm_cost/(farm*farm_rate + start_rate)

    while True:
        farms += 1.0
        farm_time = farms_time(farm_time, farms-1.0)  # time for building one more farm
        new_time = time_req(farms, farm_time)     # time to targe with the new farm
        if new_time < time: time = new_time
        else: break
    op_file.write("Case #"+str(case_num+1)+': '+str(time)+'\n')


infile.close()
op_file.close()   
        






