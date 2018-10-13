

with open("B-large.in", 'r') as f:
    with open("output.txt", 'w') as fout:
        numcases = int(f.readline())
        for case in range(1, numcases+1):
            line = f.readline().split()
            numboosters = int(line[0])
            constructtime = int(line[1])
            targetstar = int(line[2])
            loopsize = int(line[3])
            dists = [(i-4, int(line[i])) for i in range(4, len(line))]

            
            sumdists = sum((i[1] for i in dists))
            remainder = constructtime % (2*sumdists)
            earlyloops = constructtime // (2*sumdists)
            
            remainderindex = 0
            for i in dists:
                if remainder >= 2*i[1]:
                    remainder -= 2*i[1]
                    remainderindex += 1
                else:
                    break
            dists.append((None, dists[remainderindex][1]-remainder/2))
            dists.sort(key=(lambda x: x[1]), reverse=True)

            totalloops = targetstar // loopsize
            targetremainder = targetstar % loopsize
            time = 0
            for i in dists:
                if (i[0] != None):
                    neededloops = totalloops
                    if (targetremainder > i[0]):
                        neededloops += 1
                    if (remainderindex == i[0]):
                        neededloops -= 1
                    boostableloops = neededloops-earlyloops
                    if (remainderindex > i[0]):
                        boostableloops -= 1
                    boostableloops = max((boostableloops, 0))
                    boostedloops = min((numboosters, boostableloops))
                    numboosters -= boostedloops
                    time += i[1]*(neededloops*2-boostedloops)
                    
                else:
                    if numboosters > 0:
                        numboosters -= 1
                        time += i[1]+remainder
                        
                    else:
                        time += 2*i[1]+remainder
                        

            fout.write("Case #" + str(case) + ": " + str(int(time)) +"\n")

            
