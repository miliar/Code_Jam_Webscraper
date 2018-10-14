def solveSmall(r,y,b):
    
    n = r+y+b

    if(r>n//2 or y>n//2 or b>n//2):
        return "IMPOSSIBLE"

    if(r==0 or y==0 or b==0):
        if n%2 == 1:
            return "IMPOSSIBLE"
        elif r==0:
            return "BY"*b
        elif y==0:
            return "RB"*r
        elif b==0:
            return "YR"*y
        else:
            return "ERROR"

    result = ["R","Y","B"]
    r -= 1
    b -= 1
    y -= 1
    while(r+b+y>0):
        result = result[1:] + [result[0]]
        if result[0:2].count('Y')==0 and y>0:
            result = [result[0]] + ["Y"]  + [result[1]] + result[2:]
            y -= 1
        elif result[0:2].count('B')==0 and b>0:
            result = [result[0]] + ["B"]  + [result[1]] + result[2:]
            b -= 1
        elif result[0:2].count('R')==0 and r>0:
            result = [result[0]] + ["R"]  + [result[1]] + result[2:]
            r -= 1

    return "".join(result)

def check(result, r, y, b):
    if result.count('R')==r and result.count('Y')==y and result.count('B')==b:
        if result[0] == result[-1]:
            return False
        while(len(result)>=2):
            if result[0]==result[1]:
                return False
            result = result[1:]
        return True
    return False

def solve(r,o,y,g,b,v):
    if o==0 and g==0 and v==0:
        return solveSmall(r,y,b)
    else:
        return "NOT IMPLEMENTED"

t = int(input())
for i in range(1,t+1):
    n, r, o, y, g, b, v = [int(x) for x in input().split(" ")]
    print("Case #" + str(i) + ": " + solve(r,o,y,g,b,v))
    if(solve(r,o,y,g,b,v) != "IMPOSSIBLE" and not check(solve(r,o,y,g,b,v),r,y,b)):
        print("BUG")
