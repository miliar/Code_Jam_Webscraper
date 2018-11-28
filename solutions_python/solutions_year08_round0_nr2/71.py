
def read_file(filepath):
    try:
        lines = file(filepath, 'rU').readlines()
    except IOError, e:
        print '*** file open failed:', filepath
        raise e
    else:
        return lines

def get_min(hm):
    h, m = hm.split(':')
    return int(h)*60 + int(m)

# main
lines = read_file('./B-large.in')
for i in range(len(lines)):
    lines[i] = lines[i].rstrip('\r\n')
print lines

N = int(lines[0])
answers = []
i = 1
for n in range(N):
    # read a case
    print 'case #'+str(n+1)+':'
    T = int(lines[i])
    i += 1
    NA, NB = lines[i].split(' ')
    i += 1
    NA = int(NA)
    NB = int(NB)
    print 'T:', T, 'NA:', NA, 'NB:', NB
    times_A = []
    times_B = []
    for _ in range(NA):
        times_A.append(lines[i].split(' '))
        i += 1
    for _ in range(NB):
        times_B.append(lines[i].split(' '))
        i += 1
    print 'times_A:', times_A
    print 'times_B:', times_B
    
    # hh:mm to min
    for j in range(NA):
        times_A[j][0] = get_min(times_A[j][0])
        times_A[j][1] = get_min(times_A[j][1]) + T
    for j in range(NB):
        times_B[j][0] = get_min(times_B[j][0])
        times_B[j][1] = get_min(times_B[j][1]) + T
    print 'times_A:', times_A
    print 'times_B:', times_B
    
    #
    time_dict = {}
    for j in range(NA):
        leave, arrive = times_A[j]
        if leave in time_dict.keys():
            time_dict[leave].append('leave_0')
        else:
            time_dict[leave] = ['leave_0']
        if arrive in time_dict.keys():
            time_dict[arrive].append('arrive_1')
        else:
            time_dict[arrive] = ['arrive_1']
    for j in range(NB):
        leave, arrive = times_B[j]
        if leave in time_dict.keys():
            time_dict[leave].append('leave_1')
        else:
            time_dict[leave] = ['leave_1']
        if arrive in time_dict.keys():
            time_dict[arrive].append('arrive_0')
        else:
            time_dict[arrive] = ['arrive_0']
    
    for time in sorted(time_dict.keys()):
        time_dict[time] = sorted(time_dict[time])
        print time, time_dict[time]
    
    # solve
    trains_leave = [0, 0]
    trains_ready = [0, 0]
    for time in sorted(time_dict.keys()):
        for command in time_dict[time]:
            action, station = command.split('_')
            station = int(station)
            if action=='arrive':
                trains_ready[station] += 1
            elif action=='leave':
                if trains_ready[station]==0:
                    trains_leave[station] += 1
                else:
                    trains_ready[station] -= 1
            else:
                print 'illegal command:', command
                exit(1)
            print time, action, station, trains_leave, trains_ready
    answers.append(trains_leave)
    
# answers
for n in range(N):
    print 'Case #'+str(n+1)+':', answers[n][0], answers[n][1]

