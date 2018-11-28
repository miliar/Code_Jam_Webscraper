import sys

num_case = int(sys.stdin.readline())

for m in range(1, num_case + 1):
#for n in range(2):
    lst = sys.stdin.readline().split()
    C = float(lst[0])
    F = float(lst[1])
    X = float(lst[2])
    
    n = X
    num_farms = 0
    time = 0.0
    
    
    if n <= 2:
        time = time + (n / 2.0)
    else:
        while n >= 0:
            sec = float(C / (2 + (F * num_farms)))
        
            # Remaining time to reach goal by adding another farm
            farm = float(n / (((num_farms + 1) * F) + 2)) + sec
        
            # Remaining time to reach goal by not adding another farm
            no_farm = float(n / (2 + (F * num_farms)))            
        
            # If adding a farm is more beneficial, then spend C but add a farm
            if farm < no_farm:
                num_farms = num_farms + 1
                time = time + sec
            else:
                time = time + no_farm
                break

    print("Case #%d: %0.7f" % (m, time))

    
