from operator import itemgetter

#def alg(l,t,n,pattern):
#    print( (l,t,n,pattern) )
#    dists = pattern * (1+ (n-1)/len(pattern) )
#    dists = dists[0:n]
#    print(dists)
#    
#    times = [dist/0.5 for dist in dists]
#    
#    upgrades = []
#    cnt = 0
#    for dist in dists:
#        base_time = times[cnt]
#        best_t = t
#        
#        for i in range(cnt-1,-1-1):
#           
#            
#        if (best_t >= base_time):
#            upgraded_time = base_time
#        else:
#            upgraded_time = t+(dist - (t*0.5))*1.0
#        if (upgraded_time < base_time):
#            upgrades.append( (cnt, base_time-upgraded_time, upgraded_time) )
#            
#        cnt += 1
#    
#    print(upgrades)
#    upgrades.sort(key=itemgetter(1))
#    print(upgrades)
#    
#    for i in range(min(l, len(upgrades))):
#        (i, improvement, new) = upgrades.pop()
#        times[i] = new
#
#    print(times)
#    
#    print("====")
#    return [sum(times)]


def iteration_cycle(l,t,n,times, dists):
    upgrades = []
    cnt = 0
    for dist in dists:
        if times[cnt] != dist / 0.5:
            cnt += 1
            continue
        
        base_time = times[cnt]
        
        best_t = t
        check_t = t
        for i in range(cnt-1,-1,-1):
            check_t -= times[i]
#            print(str(i)+" "+str(check_t))
            if (check_t < 0):
                best_t = 0
                break
            best_t = check_t
            
            
        if (best_t >= base_time):
            upgraded_time = base_time
        else:
            upgraded_time = best_t+(dist - (best_t*0.5))*1.0
#            print("FONUND "+str(best_t)+" "+str(base_time)+" "+str(upgraded_time))
        if (upgraded_time < base_time):
            upgrades.append( (cnt, base_time-upgraded_time, upgraded_time) )
            
        cnt += 1
    
    upgrades.sort(key=itemgetter(1))
    print(upgrades)
    if len(upgrades) == 0:
        return None
    return upgrades.pop()

def alg(l,t,n,pattern):
    print( (l,t,n,pattern) )
    dists = pattern * (1+ (n-1)/len(pattern) )
    dists = dists[0:n]
    print(dists)
    
    times = [dist/0.5 for dist in dists]
    
    for i in range(l):
        best_upgrade = iteration_cycle(l,t,n,times, dists)
        if best_upgrade == None:
            break
        (i, improvement, new) = best_upgrade
        times[i] = new
    
    print(times)
    
    print("====")
    return [int(sum(times))]



if __name__ == '__main__':
    fname = "B"
    f = open(fname+".in.txt", "r")
    f = open("/home/lawford/Desktop/"+fname+"-small-attempt0.in")
#    f = open("/home/lawford/Desktop/"+fname+"-large.in")
    num_cases = int(f.readline().split(' ')[0])
    cnt=1
    fout = open(fname+".out.txt", "w")

# 1-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        result = alg(piece1.split(' '))
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()


    for case in range(num_cases):
        line = f.readline().split(' ')
        l = int(line[0])
        t = int(line[1])
        n = int(line[2])
        c = int(line[3])
        pattern = [int(x) for x in line[4:]]
        
        result = alg(l,t,n,pattern)
        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")

# 2-part problem
#    piece1 = f.readline()
#    while piece1 != '':
#        num_lines = int(piece1)
#        lines = []
#        for i in range(0, num_lines*2-1):
##            [s,e] = map(int, f.readline().split(" "))
#            line = f.readline().strip()
#            print(line)
#            lines.append( map(int, line.split(" ")) )
#        result = alg(lines)
#        fout.write("Case #"+str(cnt)+": "+" ".join(map(str, result))+"\n")
#        piece1 = f.readline()

        cnt = cnt+1
    fout.close()
    f.close()
