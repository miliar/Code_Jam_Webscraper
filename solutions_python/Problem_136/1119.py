#!/usr/bin/env python3

count = int(input())
for i in range(1,count+1):
    cps = 2.0
    time = 0.0
    nums = input().split(" ")
    c = float(nums[0])
    f = float(nums[1])
    x = float(nums[2])

    while True:
        time_to_x = x / cps
        time_to_farm = c / cps
        time_with_farm = time_to_farm + (x / float(cps + f))

        if time_to_x <= time_with_farm:
            time += time_to_x
            break
        
        time += time_to_farm
        cps += f
    
    


    print ("Case #" + str(i) + ": " + "{0:.7f}".format(time))
