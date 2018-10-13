import sys
in_file = file(sys.argv[1], 'r')
outfile = file('test_big.out', 'w')

num_cases = int(in_file.readline())

def to_minutes(time_array):
    return [time[0]*60 + time[1] for time in time_array]
    

for case in range(1, num_cases + 1):
    num_A = num_B = 0
    T = int(in_file.readline())
    
    A_to_B, B_to_A = map(int, in_file.readline().split())
    if A_to_B:
        A_times = [in_file.readline()[:-1].split() for i in range(A_to_B)]
        A_dep, B_arriv = zip(*[[map(int, t.split(':')) for t in time]
            for time in A_times])
        A_dep = to_minutes(A_dep)
        B_arriv = to_minutes(B_arriv)
    else:
        A_dep = []
        B_arriv = []
    
    if B_to_A:
        B_times = [in_file.readline()[:-1].split() for i in range(B_to_A)]
        B_dep, A_arriv = zip(*[[map(int, t.split(':')) for t in time]
            for time in B_times])
        B_dep = to_minutes(B_dep)
        A_arriv = to_minutes(A_arriv)
    else:
        B_dep = []
        B_arriv = []
    
    for next_depart in sorted(A_dep):
        next_arrival = min(A_arriv) if A_arriv else 1500
        if next_depart < next_arrival + T:
            num_A += 1
        else:
            A_arriv.remove(next_arrival)
    
    for next_depart in sorted(B_dep):
        next_arrival = min(B_arriv) if B_arriv else 1500
        if next_depart < next_arrival + T:
            num_B += 1
        else:
            B_arriv.remove(next_arrival)
    
    outfile.write('Case #%d: %d %d\n' % (case, num_A, num_B))

outfile.close()
