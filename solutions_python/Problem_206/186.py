DEBUG=0
import math

def printd(*arg):
    if DEBUG == 1:
        print("---",arg)
    
t = int(input())  # read a line with a single integer
for case_num in range(1, t + 1):
    d, n =  [int(s) for s in input().split(" ")]
    other_horses_times = []
    max_time = 0
    for i in range(n):
        k,s = [int(s) for s in input().split(" ")]
        time=(d-k)/s
        if time > max_time:
            max_time = time
    printd(other_horses_times)
    printd("max time: ", max_time)
    speed = d / max_time
    printd("speed: ", speed)
    print("Case #{}: {}".format(case_num, speed))
    
    
