import math
def addPerson(c,last):
    sec = []
    dist = 0
    first = 0
    for place in range(len(c)):
        stall = c[place]
        if(place != 0):
            if(stall == "."):
                dist += 1
            elif(stall == "O"):
                section = {
                    "top": first-1,
                    "last": place,
                    "dist": dist
                }
                sec.append(section)
                dist = 0
                first = place
    highest = sec[0]
    for a in sec:
        if(a["dist"] > highest["dist"]):
            highest = a
    lowest = highest
    c = list(c)
    mid = math.ceil(float(highest["dist"])/2) + 1
    c[highest["top"]+mid] = "O"
    c = "".join(c)
    if(last == False):
        return c
    else:
        return c, (highest["top"] + mid)
def findMinMax(c,pos):
    #print(c)
    c = list(c)
    high = 0
    low = 0
    l = 0
    r = 0
    cou = pos - 1
    while(c[cou] != "O"):
        cou -= 1
        l += 1
    cou = pos + 1
    while(c[cou] != "O"):
        cou += 1
        r += 1
    if(l > r):
        high = l
        low = r
    else:
        high = r
        low = l
    return [high,low]
def solve(stalls,people):
    corridor = ""
    corridor = "O" + ("."*stalls) + "O"
    for i in range(people):
        if(i != people-1):
            corridor = addPerson(corridor, False)
        else:
            corridor, pos = addPerson(corridor, True)
            #print(pos)
    return findMinMax(corridor, pos)
t = int(input())
for i in range(1,t+1):
    s, p = [int(s) for s in input().split(" ")]
    solut = solve(s,p)
    ma = solut[0]
    mi = solut[1]
    print("Case #{}: {} {}".format(i,ma,mi))

