#!/usr/bin/python
import sys
		
data = sys.stdin.readlines()
cases = int(data.pop(0))
case = 1

def getGrid(data):
    lst = []
    for x in range(4):
        temp = data.pop(0).split()
        temp = [int(y) for y in temp]
        lst.append(temp)
    return lst

for case in range(1, cases+1):
    input = data.pop(0).split()
    FARM_COST, FARM_CPS, TARGET = [float(x) for x in input]

    cookies = 0.0
    time = 0.0
    cps = 2.0
    while(cookies < TARGET):
        diff_target = TARGET - cookies
        diff_farm = FARM_COST - cookies
        
        if cookies < FARM_COST:
            if diff_target < FARM_COST:
                cookies += diff_target
                time += diff_target / cps
                break
            cookies += diff_farm
            time += (diff_farm / cps)
            continue
        else:
            # can afford a farm. do i want to buy one?
            # look ahead in time.
            time_to_target = diff_target / cps
            
            modified_cps = cps + FARM_CPS
            modified_cookies = cookies - FARM_COST
            modified_time_to_target = (TARGET - modified_cookies) / modified_cps
            
            if time_to_target < modified_time_to_target:
                time += time_to_target
                break
            else:
                #buy a farm
                cookies = cookies - FARM_COST
                cps += FARM_CPS
        
    sys.stdout.write("Case #%d: %.8f\n" % (case, time))