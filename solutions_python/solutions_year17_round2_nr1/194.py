

def cruise_control_solve(D, pos, speeds):
    max_speed = float(D * speeds[0]) / (D - pos[0])
    for i in xrange(1, len(pos)):
        max_speed = min(float(D * speeds[i]) / (D - pos[i]), max_speed)
    return max_speed

def cruise_control_main(input_filename, output_filename):
    f = open(input_filename, "rb")
    output_f = open(output_filename, "w")
    
    T = int(f.readline().split()[0])
    
    for i in range(1, T + 1):
        inputs = f.readline().split()
        D = int(inputs[0])
        N = int(inputs[1])
        pos = []
        speeds = []
        for j in xrange(N):
            inputs = f.readline().split()
            pos.append(int(inputs[0]))
            speeds.append(int(inputs[1]))

        max_speed = cruise_control_solve(D, pos, speeds)
        #print max_speed
        
        output_f.write("Case #" + str(i) + ": " + str(max_speed) + "\n")
    return 1

cruise_control_main("A-large.in", "A-large.out")
        
