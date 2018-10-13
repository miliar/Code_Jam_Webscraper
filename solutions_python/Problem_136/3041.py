input_file = open('B-large.in','r')
raw_input = input_file.read()

lines = raw_input.split('\n')

num_cases = int(lines[0])
case_num = 1

output_text = ''
output_file = open('2.out','w')

C,F,X = 0.,0.,0.
time_left,time,cookies = 0.,0.,0.
rate = 2.

debug=0 #0 for nothing, 1 for answer, 2 for all

while case_num<=num_cases:
    C,F,X = map(float,lines[case_num].split(' '))
    t_payoff = C/F
    time_left = X/2.0
    time = 0.
    cookies=0.
    rate=2.
    
    if debug==2:
        print('\nCase #'+str(case_num)+': C,F,X')
        print(C,F,X)
        print('time for factory payoff, rate')
        print(t_payoff,rate)

    while time_left>0:
        if debug==2: print('cookies,time,t_left = '+str(cookies)+','+str(time)+','+str(time_left))
        if cookies>=C and t_payoff<time_left:
            cookies -= C
            rate += F
            if debug==2: print('  Bought factory. cookies,rate = '+str(cookies)+','+str(rate))
        
        time_to_next_factory = (C-cookies)/rate
        time_left = (X-cookies)/rate

        if debug==2: print('time_to_next,t_left = '+str(time_to_next_factory)+','+str(time_left))
        if time_to_next_factory + t_payoff >= time_left:
            time += time_left
            time_left = 0
            if debug==2: print('Finished in time '+str(time)+'\n')
            output_text += 'Case #'+str(case_num)+': '+str(round(time,8))+'\n'
        else:
            time += time_to_next_factory
            cookies += C #rate*time_to_next_factory
            time_left -= time_to_next_factory
            if debug==2: print('  Moved along') #. cookies,time,t_left = '+str(cookies)+','+str(time)+','+str(time_left))
    
    case_num += 1

if debug: print(output_text)
output_file.write(output_text)
input_file.close()
output_file.close()
