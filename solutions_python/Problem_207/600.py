def stable(n, r, o, y, g, b, v):
    #small dataset o = g = v = 0
    if (r > y + b) or (y > r + b) or (b > r + y):
	   return "IMPOSSIBLE"
    order = list()
    if r == max(r, y, b):
        order.append("R")
        r -= 1
    elif y == max(r, y, b):
        order.append("Y")
        y -= 1
    else:
        order.append("B")
        b -= 1

    while (r > 0) or (y > 0) or (b > 0): 
        if order[-1] == 'R':
            if y == b:
                if order[0] == 'Y':
                    order.append('Y')
                    y -= 1
                else:
                    order.append('B')
                    b -= 1
            elif y == max(y, b):
                order.append('Y')
                y -= 1
            else:
                order.append('B')
                b -= 1
        elif order[-1] == 'Y':
            if r == b:
                if order[0] == 'R':
                    order.append('R')
                    r -= 1
                else:
                    order.append('B')
                    b -= 1
            elif r == max(r, b):
                order.append('R')
                r -= 1
            else:
                order.append('B')
                b -= 1
        else:
            if r == y:
                if order[0] == 'R':
                    order.append('R')
                    r -= 1
                else:
                    order.append('Y')
                    y -= 1
            elif r == max(r, y):
                order.append('R')
                r -= 1
            else:
                order.append('Y')
                y -= 1

    return ''.join(order) 

if __name__ == '__main__':
    for T in range(int(raw_input().strip())):
        n, r, o, y, g, b, v = (int(n) for n in raw_input().strip().split())
        print "Case #%d: %s" % (T+1, stable(n, r, o, y, g, b, v))