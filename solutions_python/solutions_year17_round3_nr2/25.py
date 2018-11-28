
def parenting_partnering_solve(cam_start, cam_end, jam_start, jam_end):
    cam_time = 720
    jam_time = 720
    for i in range(len(cam_start)):
        cam_time -= (cam_end[i] - cam_start[i])
    for i in range(len(jam_start)):
        jam_time -= (jam_end[i] - jam_start[i])

    all_events = []
    for i in range(len(cam_start)):
        all_events.append((cam_start[i], cam_end[i], "c"))    
    for i in range(len(jam_start)):
        all_events.append((jam_start[i], jam_end[i], "j"))
    all_events.sort(key=lambda x: x[0])

    cam_bridges = []
    for i in range(0, len(all_events) - 1):
        if all_events[i][2] == "c" and all_events[i+1][2] == "c":
            cam_bridges.append(all_events[i+1][0] - all_events[i][1])
    if all_events[-1][2] == "c" and all_events[0][2] == "c":
        cam_bridges.append(all_events[0][0] + 1440 - all_events[-1][1])

    jam_bridges = []
    for i in range(0, len(all_events) - 1):
        if all_events[i][2] == "j" and all_events[i+1][2] == "j":
            jam_bridges.append(all_events[i+1][0] - all_events[i][1])
    if all_events[-1][2] == "j" and all_events[0][2] == "j":
        jam_bridges.append(all_events[0][0] + 1440 - all_events[-1][1])

    min_switches = 0
    for i in range(0, len(all_events) - 1):
        if all_events[i][2] != all_events[i+1][2]:
            min_switches += 1
    if all_events[-1][2] != all_events[0][2]:
        min_switches += 1
    #print cam_bridges, cam_time
    #print jam_bridges, jam_time
    cam_bridges.sort()
    if len(cam_bridges) > 0:
        while cam_time >= cam_bridges[0]:
            cam_time -= cam_bridges[0]
            cam_bridges.remove(min(cam_bridges))
            cam_bridges.sort()
            if len(cam_bridges) == 0:
                break
    if len(jam_bridges) > 0:
        jam_bridges.sort()
        while jam_time >= jam_bridges[0]:
            jam_time -= jam_bridges[0]
            jam_bridges.remove(min(jam_bridges))
            jam_bridges.sort()
            if len(jam_bridges) == 0:
                break

    min_switches += 2 * len(cam_bridges)
    min_switches += 2 * len(jam_bridges)
    return min_switches

def parenting_partnering_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    
    for i in range(1, T + 1):
        inputs = f.readline().split()
        A_c = int(inputs[0])
        A_j = int(inputs[1])

        cam_start = []
        cam_end = []
        jam_start = []
        jam_end = []
        for j in xrange(A_c):
            inputs = [int(x) for x in f.readline().split()]
            cam_start.append(inputs[0])
            cam_end.append(inputs[1])
            
        for j in xrange(A_j):
            inputs = [int(x) for x in f.readline().split()]
            jam_start.append(inputs[0])
            jam_end.append(inputs[1])

        #print N, horse_cap, horse_speed, edges, targets
        sol = parenting_partnering_solve(cam_start, cam_end, jam_start, jam_end)
        #print sol
        str_sol = " ".join([str(x) for x in [sol]])
        output_f.write("Case #" + str(i) + ": " + str_sol + "\n")
    return 1

parenting_partnering_main("B-large.in", "B-large.out")
