INPUT_FILE = 'inputs/A-large.in'
OUTPUT_FILE = 'outputs/A-large.out'

f_in = open(INPUT_FILE, 'r')
f_out = open(OUTPUT_FILE, 'w+')

T = int(f_in.readline())

for t in range(T):
    N, K = [int(i) for i in f_in.readline().split()]
    lightStatus = 'OFF'
    # the light will be on if and only if (K + 1) % (2 ^ N) == 0
    if ((K + 1) % (1 << N) == 0):
        lightStatus = 'ON'

    f_out.write("Case #" + str(t + 1) + ": " + lightStatus + "\n")
    
f_in.close()
f_out.close() 