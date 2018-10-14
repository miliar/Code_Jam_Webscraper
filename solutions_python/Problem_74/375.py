import math

f = open('a.in')
cases = int(f.readline())
case = 1
while case<=cases:
    task = f.readline()
    split_nums = int(task.split(' ', 1)[0])
    task_line = task.split(' ', 1)[1]
    position = 0
    
    position_b = 1
    position_o = 1
    
    total_time = 0
    time_b = 0
    time_o = 0
    
    while position<split_nums:
        which_bot = task_line.split(' ', 2)[0]
        which_button = int(task_line.split(' ', 2)[1])
        
        if (which_bot.strip() == 'B'):
            time_b += abs(position_b - which_button)+1
            position_b = which_button
            if (time_o>=time_b):
                time_b = time_o + 1
                
            
        if (which_bot.strip() == 'O'):
            time_o += abs(position_o - which_button)+1
            position_o = which_button
            if (time_b>=time_o):
                time_o = time_b + 1
                      
        if (len(task_line.split(' ', 2))>2):
            task_line = task_line.split(' ', 2)[2]
            
        position += 1
        
               
    total_time = max(time_b, time_o)   
    print "Case #"+str(case)+": "+str(total_time)
    case += 1