from math import ceil

def fill_stalls(stalls, color, start, gap):
    for x in range(start, len(stalls), gap):
        stalls[x] = color

def first_empty_stall(stalls):
    for x in range(len(stalls)):
        if stalls[x] == " ":
            return x

t = int(input())

for x in range(1, t + 1):
    n, r, o, y, g, b, v = [int(s) for s in input().split(" ")]

    colors = [[r, 0, 0, "R"], [o, 0, 2, "O"], [y, 0, 0, "Y"], [g, 0, 2, "G"], [b, 0, 0, "B"], [v, 0, 2, "V"]]

    if r < g or  y < v or b < o or 2*r > n or 2*y > n or 2*b > n:
        print("Case #{0}: IMPOSSIBLE".format(x))
        continue
    stalls = [" "]*n

    prev = ''

    for i in range(len(stalls)): 
    
        if prev == '':
            m = max(colors)
        elif prev == 'R':
            m = max(colors[2], colors[3], colors[4])
        elif prev == 'O':
            m = colors[4]
        elif prev == 'Y':
            m = max(colors[4], colors[5], colors[0])
        elif prev == 'G':
            m = colors[0]
        elif prev == 'B':
            m = max(colors[0:3])
        elif prev == 'V':
            m = colors[2]

        index = colors.index(m)
         
        colors[index][0] -= 1
        colors[index][1] += 1
        prev = m[3] 

        stalls[i] = m[3]

    print("Case #{0}: {1}".format(x, "".join(stalls)))

    """
    total_r = r + o + v
    total_y = o + y + g
    total_b = g + b + v

    total_r = r
    total_y = y
    total_b = b

    if total_r >= total_y and total_r >= total_b:
        fill_stalls(stalls, "R", 0, ceil(float(n)/r))
        
        print(stalls)

        if total_y >= total_b:
            fill_stalls(stalls, "Y", 1, ceil(float(n)/y))
            if b > 0:
                fill_stalls(stalls, "B", 2, ceil(float(n)/b))
        else:
            fill_stalls(stalls, "B", 1, ceil(float(n)/b))
            if y > 0:
                fill_stalls(stalls, "Y", 2, ceil(float(n)/y))
    elif total_y >= total_b and total_y >= total_r:
        fill_stalls(stalls, "Y", 0, ceil(float(n)/y))

        print(stalls)

        if total_r >= total_b:
            fill_stalls(stalls, "R", 1, ceil(float(n)/r))
            if b > 0:
                fill_stalls(stalls, "B", 2, ceil(float(n)/b))
        else:
            fill_stalls(stalls, "B", 1, ceil(float(n)/b))
            if r > 0:
                fill_stalls(stalls, "R", 2, ceil(float(n)/r))

    elif total_b >= total_r and total_b >= total_y:
        fill_stalls(stalls, "B", 0, ceil(float(n)/b))

        print(stalls)

        if total_y >= total_r:
            fill_stalls(stalls, "Y", 1, ceil(float(n)/y))
            if r > 0:
                fill_stalls(stalls, "R", 2, ceil(float(n)/r))
        else:
            fill_stalls(stalls, "R", 1, ceil(float(n)/r))
            if y > 0:
                fill_stalls(stalls, "Y", 2, ceil(float(n)/y))


    print("Case #{0}: {1}".format(i, "".join(stalls)))
    """

    
