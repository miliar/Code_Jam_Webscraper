
filename = "B-large"

file = open(filename + '.in.txt')
output_file = open(filename+'.output.txt', 'w')

test_cases = int(file.readline())


for tc in range(1,test_cases + 1):
    
    line = file.readline()
    
    cost,farm,target  = map(float, line.strip().split())
    rate = 2.0
    seconds = cost / rate
    
    while(True):
        time_without_farm = (target - cost) / rate
        time_with_farm = target / (rate + farm)
        
        if time_with_farm < time_without_farm:
            rate += farm
            seconds +=  cost / rate
        else:
            seconds += time_without_farm
            break
            
    
    result = "%.7f" % seconds
    print('Case #',tc,': ',result, sep="")
    output_file.write('Case #' + str(tc) + ': ' + result + '\n')