from time import time
import psyco
import re
psyco.full()

fin = open("train_input.txt","r")
fout = open("train_output.txt","w")
cases = int(fin.readline())

def next_trains(time, list):
    return [(a,b) for (a,b) in list if a >= time]

t0 = time()
for casenr in range(cases):
    print "CASE: ",(casenr+1)
    turn = int(fin.readline())
    (na,nb) = map(int, fin.readline().split())
    
    trains = [[],[]]
    froma = 0
    fromb = 1
    
    total_trains = [0,0]
    
    p = re.compile('(\d+):(\d+) (\d+):(\d+)')
    for i in range(na):
        m = p.match(fin.readline())
        starttime = int(m.group(1)) * 60 +  int(m.group(2))
        endtime = int(m.group(3)) * 60 +  int(m.group(4))
        trains[froma].append((starttime,endtime))

    for i in range(nb):
        m = p.match(fin.readline())
        starttime = int(m.group(1)) * 60 +  int(m.group(2))
        endtime = int(m.group(3)) * 60 +  int(m.group(4))
        trains[fromb].append((starttime,endtime))  
    
    trains[froma].sort()
    trains[fromb].sort()
        
    while trains[froma] and trains[fromb]:
        print trains
        train_from = froma
        train_index = 0
        if (trains[froma][0][0] > trains[fromb][0][0]):
            train_from = fromb
        total_trains[train_from] += 1
            
        while train_from >= 0:
            arrival = trains[train_from][train_index][1]
            trains[train_from].pop(train_index)
            current_station = 1 - train_from
            nexttrains = next_trains(arrival + turn, trains[current_station])
            print arrival,turn, nexttrains
            if nexttrains:
                train_from = current_station
                train_index = trains[train_from].index(nexttrains[0])
            else:
                train_from = -1
            
        
    fout.write("Case #%d: %d %d" % (casenr+1, total_trains[0] + len(trains[froma]), 
                                        total_trains[1] + len(trains[fromb])) + "\n")
    
         
    


print "Time taken: ", time()-t0
    
    
    
    
    
    