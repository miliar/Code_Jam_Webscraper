import sys
lines = open(sys.argv[1]).read().splitlines()
fp = open('OUTPUT.txt', 'w')

num_cases = int(lines.pop(0))
for case in range(num_cases):
    num_logs = int(lines.pop(0))
    naomi_logs = [float(v) for v in lines.pop(0).split()]
    sorted_naomi_logs = sorted(naomi_logs)
    ken_logs = [float(v) for v in lines.pop(0).split()]

    cheat = 0
    for ken_log in ken_logs:    
        this_log = None
        for naomi_log in sorted_naomi_logs:
            if naomi_log > ken_log:
                this_log = naomi_log
                cheat += 1
                break
        if this_log is None:
            this_log = sorted_naomi_logs[0]
        sorted_naomi_logs.remove(this_log)
            
    ken_logs.sort()
    score = 0
    for naomi_log in naomi_logs:
        this_log = None
        for ken_log in ken_logs:
            if ken_log > naomi_log:
                this_log = ken_log
                score += 1
                break

        if this_log is None:
            this_log = ken_logs[0]
        ken_logs.remove(this_log)
    #print cheat, num_logs - score

    fp.write('Case #{}: {} {}\n'.format(case + 1, cheat, num_logs - score))

fp.close()
