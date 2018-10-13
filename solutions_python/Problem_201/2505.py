def main():
    cases = int(input())

    for i in range(1, cases + 1):
        case = input()
        stalls,people = case.split()
        ans = solve(int(stalls), int(people))
        s = "Case #" + repr(i) + ":"
        print(s,ans[0], ans[1])


def solve(num_stalls, people):

    stalls = []
    stalls.append(1)
    for i in range(0,num_stalls):
        stalls.append(0)
    stalls.append(1)

    l = 0
    r = num_stalls-1
    high_min = 0
    spot = 1
    for i in range(0, people):
        if i == people - 1: 
            ans = get_min(stalls,1)
        get_min(stalls,0)
        
    return ans


def get_min(stalls,last ):
    l = 0
    r = 0
    
    room = []
    for i in range(1, len(stalls)-1):
        curr = i
        if stalls[curr] == 1:
            continue
        while stalls[curr-1] != 1:
            curr -= 1
            l += 1
        curr = i
        while stalls[curr+1] != 1:
            curr += 1
            r += 1
        room.append((l,r,i))
        l = 0
        r = 0

    choose = []
    fc = 0
    for r in room:
        if min(r[0],r[1]) > fc:
            choose = []
            choose.append(r)
            fc = min(r[0],r[1])
        elif min(r[0],r[1]) == fc:
            choose.append(r)


    if len(choose) == 0:
        return
    if len(choose) == 1:
        stalls[choose[0][2]] = 1
        return max(choose[0][0], choose[0][1]),min(choose[0][0], choose[0][1])
        

    choose2 = []
    ff = 0
    for c in choose:
        if max(c[0],c[1]) > ff:
            choose2 = []
            choose2.append(c)
            ff = max(c[0],c[1])
        elif max(c[0],c[1]) == ff:
            choose2.append(c)
    stalls[choose2[0][2]] = 1

    if last == 1:
        return max(choose2[0][0], choose2[0][1]),min(choose2[0][0], choose2[0][1])
    


if __name__ == '__main__':
    main()
