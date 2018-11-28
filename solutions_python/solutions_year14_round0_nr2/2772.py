#!/usr/bin/python3


T = int(input())

for t in range(T):
    
    C, F, X = map(float, input().split())
    
    time = 0
    cookies_per_second = 2
    while True:
        
        time_to_buy_and_reach = C/cookies_per_second + X/(cookies_per_second+F)
        time_to_reach = X/cookies_per_second
        
        if time_to_buy_and_reach < time_to_reach:
            time += C/cookies_per_second
            cookies_per_second += F
        else:
            time += time_to_reach
            break
    
    print("Case #%d: %0.7f" % (t+1, time))



