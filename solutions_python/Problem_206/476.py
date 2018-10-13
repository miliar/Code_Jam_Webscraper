

def result(distance, horses):
    times = [(distance-pos)/speed for pos,speed in horses]
    maxtimes= max(times)    
    return distance/maxtimes
    #print(horses)


t = int(input()) 

for i in range(1, t + 1):    
    
    d,n = [int(k) for k in input().split(" ")]
    horses = []
    for ii in range(n):
        pos,speed = [int(k) for k in input().split(" ")]
        horses.append((pos,speed))   
    sortedhorses = sorted(horses,key=lambda x:x[0])
    avgspeed = result(d,sortedhorses)
    print("Case #{}: {} ".format(i, avgspeed))
    

    
    
    
    