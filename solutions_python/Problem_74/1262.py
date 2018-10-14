infile = open('A-large.in')
outfile = open('A-large.out','w')
num_inputs = int(infile.readline().strip())

for case in xrange(1,num_inputs+1):
    case_data = infile.readline().strip()
    case_data = case_data.split(' ')[1:]
    prev_loc = {'O':1,'B':1}
    time_buffer = {'O':0,'B':0}
    other_guy = {'O':'B','B':'O'}
    total_time = 0
    prev_guy = case_data[0]
    for i in xrange(len(case_data)):
        if i%2 == 1:
            continue
        curr_guy = case_data[i]
        if prev_guy == curr_guy:
            move_time = abs(prev_loc[curr_guy] - int(case_data[i+1]))
        else:
            move_time = abs(prev_loc[curr_guy] - int(case_data[i+1])) - time_buffer[curr_guy]
            if move_time < 0:
                move_time = 0
        time = move_time + 1
        time_buffer[other_guy[curr_guy]] += time
        total_time += time    
        prev_loc[curr_guy] = int(case_data[i+1])
        time_buffer[curr_guy] = 0
        prev_guy = curr_guy
    outfile.write('Case #%s: %s\n' %(case, total_time))
outfile.close()
