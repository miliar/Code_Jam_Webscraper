import sys
from numpy import zeros

linect = 0
testcases = []
with open("test.in", 'r') as inp:
    for line in inp:
            token = line.split()
            linect +=1
            if linect == 1:
                testno = int(token[0])
                continue
            current_test = [int(token[0]), int(token[1])]
            testcases.append(current_test[:])
            
if linect != testno + 1:
    print ("No. of test cases do not match the number given in the file. Exiting...")
    sys.exit(1)    
            
with open("test.out", 'w') as out:
    for test_idx in  range(testno):
        devicect = testcases[test_idx][0]
        snapct = testcases[test_idx][1]
        power_in = zeros(devicect + 1)
        power_out = zeros(devicect)
        state = zeros(devicect)
        power_in[0] = 1
        for snap_idx in range(snapct):
# snap all the devices
            for device_idx in range(devicect):
                if power_in[device_idx] == 1:
                    state[device_idx] = not(state[device_idx])
                    
            for device_idx in range(devicect):       
                if state[device_idx] == 1:
                    if power_in[device_idx] == 1:
                        power_out[device_idx] = 1
                elif state[device_idx] == 0:
                    power_out[device_idx] = 0  
                     
                power_in[device_idx + 1] = power_out[device_idx]
                                
            
        if power_in[devicect] == 1:
            light_status = "ON"
        else:
            light_status = "OFF"   
        del power_in
        del power_out
        del state     
        outstring = "Case #" + str(test_idx + 1) + ": " + light_status + "\n"
        out.write(outstring)
        
print ("Everything Done!")        
                    