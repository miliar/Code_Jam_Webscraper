file = open('B-large.in.txt', 'r')
file = file.readlines()
number_of_test_cases = int(file[0])
output = open('output.text', 'a')
foo = ""
for i in range(1, len(file)):
    cost, added_rate, cookies_needed = file[i].split()
    cost = float(cost)
    added_rate = float(added_rate)
    cookies_needed = float(cookies_needed)
    current_rate = 2
    buy = True
    prev_cookie_house = 0
    current_time = cookies_needed / current_rate 
    while buy:
        buy = False
        new_rate = current_rate + added_rate 
        time_buying = prev_cookie_house + (cookies_needed/new_rate) + (cost / current_rate)
        if current_time > time_buying:
            buy = True
            prev_cookie_house += cost/current_rate
            current_rate += added_rate
            current_time = time_buying
    foo += 'Case #{0}: {1}\n'.format(i, current_time)
output.write(foo)
output.close()
                     
    



            
        
    
