def readFile(flname):
    lines = open(flname).read().split("\n")
    outputfl = open("output.txt","w")
    testAmount = int(lines[0])
    for i in range(1,len(lines)-1):
        curTest = lines[i].split(" ")
        colors = [int(x) for x in curTest[1:]]
        curAns = solveSpecificRow(colors)
        outputfl.write("Case #"+str(i)+": "+str(curAns)+"\n")
    outputfl.close()
def solve(r,y,b):
    if r==0:
        if y==b:
            return "yb"*y
        elif y==b-1:
            return "b"+"yb"*y
        elif y==b+1:
            return "y"+"by"*b
        else:
            return "IMPOSSIBLE"
    ans=""
    while r>0:
        if y>b:
            ans+="ry"
            r-=1
            y-=1
            last="y"
        else:
            ans+="rb"
            r-=1
            b-=1
            last="b"
    #HERE r=0
    if y<0 or b<0:
        return "IMPOSSIBLE"
    if y==b:
        if last == "b":
            ans+= "yb"*y
        else:
             ans+= "by"*y
    elif y==b-1:
        if last == "y":
            ans+= "b"+"yb"*y
        else:
            return "IMPOSSIBLE"
    elif y==b+1:
        if last == "b":
            ans+= "y"+"by"*b
        else:
            return "IMPOSSIBLE"
    else:
        return "IMPOSSIBLE"
    return ans

def old(r,y,b):
    print("input "+str((r,y,b)))
    if r==0:
        if not (y==b and y+b>=1):
            return "IMPOSSIBLE"
        else:
            return "yb"*y
    
    if not (abs(y-b)<=r and y+b>=r):
        return "IMPOSSIBLE"
    else:
        ans = ""
        mx = max(y,b)
        if mx  == y:
            ans =""
            for i in range(y-b):
                ans+="ry"
                y-=1
                r-=1        
        else:
            ans =""
            for i in range(b-y):
                ans+="rb"
                b-=1
                r-=1
        for i in range(r-1):
            if y>b:
                ans+="ry"
                y-=1
                r-=1
            else:
                ans+="rb"
                b-=1
                r-=1
        ans+="r"
        r-=1
        if y>b:
            ans+="y"+b*"by"
            y-=1
            b,y=b-b,y-b
        elif b>y:
            ans+="b"+y*"yb"
            b-=1
            b,y=b-y,y-y
        else:
            ans+=y*"yb"
            b,y=b-y,y-y
        print(r,b,y)
        return ans
            
def solveSpecificRow(colors):
    (r,o,y,g,b,v)=colors
    ans = solve(r,y,b)
    return ans
    
    
