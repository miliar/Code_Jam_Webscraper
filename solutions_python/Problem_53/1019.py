input_file = open("QR_A_input.txt", "r")
input_text = input_file.readlines()
input_file.close()

output_file = open("QR_A_output.txt", "w")
case_count = int(input_text[0])
print "all case : " + str(case_count)

for case in range(case_count) :
    print "case : " + str(case)
    case_input = input_text[1 + case].split()
    
    devices_num = int(case_input[0])
    snap_times_num = int(case_input[1])
    print "input case : " + str(case_input)
    devices = [0]
    for device_count in range(devices_num - 1) :
        devices.append(0)
    devices_power = devices[:]
    devices_power[0] = 1
    print "devices : " + str(devices)
    
    last_on_off = 0

    for snap_time in range(snap_times_num) :
        # power update
        power_update_flag = 1
        for search_re in range(len(devices_power) - 1) :
            if devices[search_re] == 1 and power_update_flag == 1 :
                devices_power[search_re + 1] = 1
            else :
                devices_power[search_re + 1] = 0
                power_update_flag = 0
        #print "power : " + str(devices_power)
        if devices[0] == 0 :
            devices[0] = 1
        else :
            devices[0]  = 0
        for search_re in range(len(devices) - 1) :
            if devices_power[search_re + 1] == 1 :
                if devices[search_re + 1] == 0 :
                    devices[search_re + 1] = 1
                else :
                    devices[search_re + 1]  = 0
            else :
                break
        last_on_off = 0
        for search_re in range(len(devices)) :
            if devices[search_re] == 1 :
                if (search_re + 1) == len(devices) :
                    last_on_off = 1
                    print "power on"
            else :
                break
    if last_on_off == 1 :
        last_on_off = "ON"
    else :
        last_on_off = "OFF"
    output_file.write( "Case #" + str(case + 1) + ": " + str(last_on_off) + "\n")
#case_count = int(case_count_text)
#print case_count

output_file.close()