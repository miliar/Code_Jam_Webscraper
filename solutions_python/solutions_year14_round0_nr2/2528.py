from itertools import combinations
import sys

cnt = 0 
w = int(sys.stdin.readline().strip())


def should_buy_farm(current_pile,cost,rate,new_rate_addition,target):
    t1 = float(target - current_pile)/float(rate)
    t2 = float(target - current_pile + cost)/float(rate + new_rate_addition)


    #print "time", t1,t2
    if (t2 < t1):
        return True
    else:
        return False

while cnt < w:
    line = sys.stdin.readline()
    line = line.strip().split(' ')
    line = [ float (x) for x in line]
   
    current_pile = 0
    rate = 2
    new_rate_addition = line[1]
    cost = line[0]
    target = line[2]
    time = 0.00

    more_farms = True

    while more_farms:
        #print "rate",rate,new_rate_addition,cost,time,target,current_pile
        if(cost > target):
            #print "BREAK"
            break

        if(current_pile < cost):
            current_pile = cost
            time += float(current_pile) / float(rate)

        more_farms = should_buy_farm(current_pile,cost,rate,new_rate_addition,target)
        if more_farms:
            rate += new_rate_addition
            current_pile -= cost


    if(current_pile < target):
        time += float(target - current_pile) / float(rate)
    
    cnt += 1
    print("Case #"+str(cnt) +": %.7f" % time)
        

