def on_off(n_snappers, n_snaps):
    if n_snaps < n_snappers:
        return 'OFF'
    elif (n_snaps+1) % (2**n_snappers) == 0:
        return 'ON'
    else:
        return 'OFF'

in_file=open('A-large.in', 'r')
out_file=open('A-large.out', 'w')

t_cases=int(in_file.readline())

for case_num in range(1, t_cases+1):
    case=in_file.readline().split()
    n_snappers, n_snaps = map(int, case)
    state = on_off(n_snappers, n_snaps)
    out_file.write("Case #%s: %s\n" %(case_num, state))

in_file.close()    
out_file.close()
