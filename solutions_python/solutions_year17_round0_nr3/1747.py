import math
if __name__ == "__main__":
    n = int(raw_input())
    for i in range(n):
        test = [ int(x) for x in raw_input().strip().split() ]
        stalls = [ True for x in range(test[0]) ]
        stalls = [ False ] + stalls
        stalls.append(False)
        
        for times in range(test[1]):
            lindex = 0
            rindex = 0
            count = 0
            for index, val in enumerate(stalls):
                if not val:
                    temp = index
                    tc = 0
                    for i1 in range(index + 1, len(stalls)):
                        if not stalls[i1]:
                            if tc > count:
                                lindex = temp
                                rindex = i1
                                count = tc
                            break
                        else:
                            tc += 1
            mid = (lindex + rindex)/2
            stalls[mid] = False
        
        lcount = 0
        rcount = 0
        for m in range(mid - 1, -1, -1):
            if not stalls[m]:
                break
            else:
                lcount += 1

        for m in range(mid + 1, len(stalls)):
            if not stalls[m]:
                break
            else:
                rcount += 1
        print "Case #" + str(i+1) + ": " + str(max(lcount, rcount)) + " " + str(min(lcount, rcount)) 
