T = int(input())

for t in range(1,T+1):
    a1 = int(input())-1
    grid1 = [input().split() for i in range(4)]
    a2 = int(input())-1
    grid2 = [input().split() for i in range(4)]

    ans = [a for a in grid1[a1] if a in grid2[a2]]
    
    if(len(ans)>1):
        print("Case #%d: Bad magician!" % t)
    elif(len(ans)==0):
        print("Case #%d: Volunteer cheated!" % t)
    else:
        print("Case #%d: %s" % (t,ans[0]))
    
