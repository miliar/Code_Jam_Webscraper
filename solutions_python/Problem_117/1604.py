def isPossible(pattern, n, m) :
    placehold, horizontal,vertical, maxi, newList=[],[],[],0,[]
    for j in range(m-1,0-1,-1):
        placeholder=[]
        for i in range(n):
            placeholder.append(pattern[i][j])
        newList.append(placeholder)
        placeholder=[]
    for k in range(len(newList)):
        placeholder.append(newList.pop())
    newList = placeholder
    
    if (n==1) or (m==1):
        return "YES\n"
    else:
        for i in range(n):
            placeholder=[]
            for j in range(m):
                maxi = max(pattern[i])
                if pattern[i][j]>=maxi:
                    placeholder.append(True)
                else:
                    placeholder.append(False)
            horizontal.append(placeholder)
        for j in range(n):
            placeholder=[]
            for i in range(m):
                maxi = max(newList[i])
                if pattern[j][i]>=maxi:
                    placeholder.append(True)
                else:
                    placeholder.append(False)
            vertical.append(placeholder)
        for i in range(n):
            for j in range(m):
                if (horizontal[i][j]==True) or (vertical[i][j]==True):
                    continue
                else:
                    return "NO\n"
        else:
            return "YES\n"
        
#File IO stuff
f = open("input.in", "r")
o = open("BOutput.out", "w")

#Constants and stuff
T = eval(f.readline())
#Main loop
for i in range(T):
    #resets the pattern
    pattern = []
    
    #gets the length and breadth of the grass patch
    N , M = f.readline().strip("\n").rsplit(" ")
    N, M = eval(N), eval(M)
    #Gets line, by line
    for j in range(N):
        pattern.append(f.readline().strip("\n").split(" "))
        
    o.write("Case #{0}: {1}".format(i+1,isPossible(pattern, N, M)))
