def time_to_target(cps, target):
    return target/cps

cases = int(input())
for case in range(cases):
    farm_price, farm_cps, target = map(float, input().split(' '))
    cps = 2
    secs = 0
    while True:
        if time_to_target(cps, target) < (time_to_target(cps, farm_price) + time_to_target(cps+farm_cps, target)):
            #we're done, cheaper to just gen cookies
            print('Case #{}: {:.7f}'.format(case + 1, time_to_target(cps, target) + secs))
            break
        else:
            #buy another farm
            secs += time_to_target(cps, farm_price)
            cps += farm_cps
            
