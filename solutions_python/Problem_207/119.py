def arrangement(n, r, o, y, g, b, v):
    if (r-g==0) and (r!=0):
        if (n-r-g!=0):
            return "IMPOSSIBLE"
        else:
            result = ""
            for i in range(r):
                result += "RG"
            return result
    if (y-v==0) and (y!=0):
        if (n-y-v!=0):
            return "IMPOSSIBLE"
        else:
            result = ""
            for i in range(y):
                result += "YV"
            return result
    if (b-o==0) and (b!=0):
        if (n-b-o!=0):
            return "IMPOSSIBLE"
        else:
            result = ""
            for i in range(b):
                result += "BO"
            return result
    
    eff_r = r-g
    eff_y = y-v
    eff_b = b-o

    if eff_r < 0 or eff_y < 0 or eff_b < 0:
        return "IMPOSSIBLE"

    xr = eff_y + eff_b - eff_r
    xb = eff_r + eff_y - eff_b
    xy = eff_r + eff_b - eff_y

    if xr < 0 or xb < 0 or xy < 0:
        return "IMPOSSIBLE"

    if xr <= xb and xr <= xy:
        result = ""
        for i in range(xr):
            result += "RYB"
        for i in range(int((xb-xr)/2)):
            result += "RY"
        for i in range(int((xy-xr)/2)):
            result += "RB"
            
        rstring = ""
        bstring = ""
        ystring = ""
        for i in range(g):
            rstring += "RG"
        for i in range(o):
            bstring += "BO"
        for i in range(v):
            ystring += "YV"

        if g > 0:
            index1 = result.find("R")
            result = result[:index1] + rstring + result[index1:]
        if o > 0:
            index1 = result.find("B")
            result = result[:index1] + bstring + result[index1:]
        if v > 0:
            index1 = result.find("Y")
            result = result[:index1] + ystring + result[index1:]
        return result
    elif xb <= xr and xb <= xy:
        result = ""
        for i in range(xb):
            result += "BRY"
        for i in range(int((xr-xb)/2)):
            result += "BY"
        for i in range(int((xy-xb)/2)):
            result += "BR"
            
        rstring = ""
        bstring = ""
        ystring = ""
        for i in range(g):
            rstring += "RG"
        for i in range(o):
            bstring += "BO"
        for i in range(v):
            ystring += "YV"

        if g > 0:
            index1 = result.find("R")
            result = result[:index1] + rstring + result[index1:]
        if o > 0:
            index1 = result.find("B")
            result = result[:index1] + bstring + result[index1:]
        if v > 0:
            index1 = result.find("Y")
            result = result[:index1] + ystring + result[index1:]
        return result
    else:
        result = ""
        for i in range(xy):
            result += "YBR"
        for i in range(int((xr-xy)/2)):
            result += "YB"
        for i in range(int((xb-xy)/2)):
            result += "YR"
            
        rstring = ""
        bstring = ""
        ystring = ""
        for i in range(g):
            rstring += "RG"
        for i in range(o):
            bstring += "BO"
        for i in range(v):
            ystring += "YV"

        if g > 0:
            index1 = result.find("R")
            result = result[:index1] + rstring + result[index1:]
        if o > 0:
            index1 = result.find("B")
            result = result[:index1] + bstring + result[index1:]
        if v > 0:
            index1 = result.find("Y")
            result = result[:index1] + ystring + result[index1:]
        return result

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, r, o, y, g, b, v = input().split(" ")
    n = int(n)
    r = int(r)
    o = int(o)
    y = int(y)
    g = int(g)
    b = int(b)
    v = int(v)
    result = arrangement(n, r, o, y, g, b, v)
    print("Case #{}: {}".format(i, result))
