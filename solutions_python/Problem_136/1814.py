with open ("problem-B.txt", "r") as problem:
    problem_text=problem.read()
lines = problem_text.split('\n')
cases = int(lines[0])
for i in range(cases):
    rate = 2
    current_line = lines[i+1]
    values = current_line.split(' ')
    cost  = float(values[0])#C
    extra = float(values[1])#F
    max   = float(values[2])#X
    total_seconds = 0
    while ( True ):
        new_time_max = cost / rate
        total_seconds += new_time_max
        if ( new_time_max >=  max / rate ):
            total_seconds = (max) / rate
            break
        if ( ((max - cost) / rate ) <= (max/(rate+extra)) ):
            total_seconds += (max - cost) / rate
            break
        else:
            rate += extra
    total_seconds = round(total_seconds,7)
    print("Case #"+str(i+1)+": "+str(total_seconds))