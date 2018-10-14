import sys
import copy
T = int(sys.stdin.readline())
for t in range(T):
    D = int(sys.stdin.readline())
    P = [int(x) for x in sys.stdin.readline().split()]
    
    min_elapsed_time = max(P)
    
    max_chunk = max(P)
    
    divided_chunk = 2
    while divided_chunk < min_elapsed_time:
        num_of_additional_diners = 0
        for p in P:
            num_of_additional_diners += (p-1)/divided_chunk
        min_elapsed_time = min(min_elapsed_time, num_of_additional_diners + divided_chunk)

        divided_chunk += 1


    print "Case #%d: %d" % (t+1, min_elapsed_time)