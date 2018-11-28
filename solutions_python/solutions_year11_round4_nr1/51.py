
file = 'A-large'

def algorithm():
    pass

def process():
    c_length, walking, running, run_time, num_walkaway = [ int(x) for x in fin.readline().rstrip().split(' ')]
    walkaways = []
    for i in range(0, num_walkaway):
        start, end, speed = [int(x) for x in fin.readline().rstrip().split(' ')]
        walkaways.append((speed, end-start))
        c_length -= (end-start)
    walkaways.append((0, c_length))
    list.sort(walkaways)
    print walkaways
    print running
    print walking
    time = 0.0
    for segment in walkaways:
        if_all_run = segment[1]*1.0 / (segment[0] + running)
        if run_time > if_all_run:
            time += if_all_run
            run_time -= if_all_run
        else:
            left_distance = segment[1] - run_time * (segment[0] + running)
            left_time = left_distance *1.0/ (walking+segment[0])
            time += (run_time + left_time)
            run_time = 0
        print run_time, time
    return str(time)
            

fin = open(file + '.in', 'r')
fout = open(file + '.out', 'w')

num_cases = int(fin.readline().rstrip())

for i in range(1, num_cases + 1):
    result = process()
    fout.write('Case #%d: %s\n' % (i, result))

fin.close()
fout.close()