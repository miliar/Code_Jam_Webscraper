n = int(input())

for i in range(n):
    
    C, F, X = [float(a) for a in input().split()]
    
    time = 0
    rate = 2
    m = float('inf')
    
    while True:
        
        done = time + X / rate
        if done > m:
            break
        m = done
        rate, time = rate + F, time + C / rate
    
    print("Case #" + str(i + 1) + ": " + str(m))