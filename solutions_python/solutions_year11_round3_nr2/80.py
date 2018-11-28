def solve(boost, time, stars, dists, numstar, numtime):
    if numstar == stars:
        return 0

    if boost == 0 or numtime > time: # Tous les boosters peuvent etres construits
        total = 0
        gains = []
        for i in range(numstar, stars):
            gain = dist(dists, i)
            d = gain * 2

            gains.append(gain)

            #if len(gains) < boost:
                #gains.append(gain)
            #else:
                #i = 0
                #while i < len(gains):
                    #if gains[i] < gain:
                        #gains = gains[i][i]
            
            total += d

        gains.sort(reverse=True)
            
        return total - sum(gains[:boost])        
    else:
        dist_star = dist(dists, numstar)
        time_etape = dist_star * 2
        time_arriv = numtime + time_etape
        if boost == 0 or time_arriv < time: # Ne profite pas du boost
            return time_etape + solve(boost, time, stars, dists, numstar + 1, time_arriv)
        else:
            rest_time_boost = max(0, time - numtime) # Parcours sans boost
            time_boost = rest_time_boost + (dist_star - (rest_time_boost/2)) # Duree parcours
            #print (rest_time_boost, time_boost, dist_star ,(dist_star - (rest_time_boost/2)))

            active_boost = time_boost + solve(boost - 1, time, stars, dists, numstar + 1, numtime + time_boost)
            no_boost = time_etape + solve(boost, time, stars, dists, numstar + 1, time_arriv)
            return min(active_boost, no_boost)

def dist(dists, n):
    return dists[n%len(dists)]

n_tests = int(input())
for t in range(0, n_tests):
    li = [ int(i) for i in input().split(" ") ]
    boost = li[0]
    time = li[1]
    stars = li[2]
    ndists = li[3]
    dists = li[4:]

    ret = solve(boost, time, stars, dists, 0, 0)
    print ("Case #"+str(t+1)+": "+str(int(ret)))