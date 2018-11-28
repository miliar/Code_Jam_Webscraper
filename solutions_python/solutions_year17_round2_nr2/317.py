
unistrs = "ROYGBV"
def to_string(unilist):
    return "".join(unistrs[i] for i in unilist)

T = int(input())
for case in range(T):
    vals = input().split()
    N,R,O,Y,G,B,V = [int(v) for v in vals]
    
    colors = [R,O,Y,G,B,V]
    avoid = {
        0:{0,1,5},
        1:{0,1,2,3,5},
        2:{1,2,3},
        3:{1,2,3,4,5},
        4:{3,4,5},
        5:{0,1,3,4,5},
    }
    str1 = "Case #{}: ".format(case+1)
    #are_odd_colors = any(colors[i] for i in range(1,6,2))
    no_avoid = {k:{x for x in range(6) if x not in avoid[k]} for k in range(6)}
    def run_thing():
        for i in range(6):
            #if are_odd_colors and i%2==0:
            #    continue
            for j in range(6):
                colstart = i
                colend = j
                if colors[colstart] == 0 or colors[colend] == 0:
                    continue
                
                if colend in avoid[colstart]:
                    continue
                    
                newcolors = list(colors)
                newcolors[colstart] -= 1
                newcolors[colend] -= 1
                
                unilist = [colstart]
                for newi in range(1,N):
                    viables = {uni for uni in range(6) if newcolors[uni] != 0 and unilist[newi-1] in no_avoid[uni]}
                    if not viables:
                        break
                    oddvia = [x for x in range(1,6,2) if x in viables]
                    if len(oddvia) > 0:
                        cuni = oddvia[0]
                    else:
                        cuni = max((newcolors[uni],uni) for uni in range(0,6,2) if uni in viables)[1]
                    
                    newcolors[cuni] -= 1
                    unilist.append(cuni)
                if len(unilist) == N-1:
                    if unilist[N-1-1] in no_avoid[colend]:
                        unilist.append(colend)
                        print(str1+to_string(unilist))
                        return True
        return False
                    
                
    if not run_thing():
        print(str1+"IMPOSSIBLE")
    