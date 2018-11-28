def is_light_on_or_off(num_snappers, k_num_snaps):
    if k_num_snaps < num_snappers:
        return 'OFF'
    elif (k_num_snaps+1) % (2**num_snappers) == 0:
        return 'ON'
    else:
        return 'OFF'

input_file=open('A-large.in', 'r')
output_file=open('A-large.out', 'w')

test_cases=int(input_file.readline())

for case_num in range(1, test_cases+1):
    case=input_file.readline().split()
    num_snappers, k_num_snaps = map(int, case)
    light = is_light_on_or_off(num_snappers, k_num_snaps)
    output_file.write("Case #%s: %s\n" %(case_num, light))
    
output_file.close()
