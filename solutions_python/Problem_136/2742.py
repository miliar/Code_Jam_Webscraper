def cookie(farm, rate, total):

    time = 0
    current_cookies = 0
    current_rate = 2.0
    current_total = total/current_rate
    while True:
        
        #calculate the time to buy a farm
        time += (farm / current_rate)
        current_rate += rate
        
        
        #check if it's better to buy new farm or wait until current ratio farm
        #production will produce total value of cookies
        next_step = time + total/current_rate
        
        if next_step > current_total:
            time = current_total
            break
        current_total = next_step
    return round(time, 7)


if __name__ == '__main__':
    
    f = open('B-large.in', 'rb')

    lines = f.readlines()
    cases = int(lines[0])
    results = []
    
    for line in lines[1:]:
        farm, rate, total = line.rstrip().split(' ')
        time = cookie(float(farm), float(rate), float(total))
        results.append(time)

    
    #write down the results to file
    output = open('outputBig.in', 'wb')

    for i in range(cases):
        a = 'Case #' + str(i+1) + ': ' + str(results[i])
        
        output.write(a + '\n')

    output.close()
    
