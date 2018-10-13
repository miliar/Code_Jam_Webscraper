#!/usr/bin/python


def solve_small(colors):
    r,b,y = colors[1], colors[5], colors[3]
    cs = [r,b,y]
    ls = ['R','B','Y']
    if max(cs) > sum(cs)/2:
        return "IMPOSSIBLE"
    else:
        oo  =[(cs[i], i) for i in range(3)]
        oo.sort()
        order = map(lambda l: l[1], oo)
        order.reverse()
        argmax = order[0]
        sn = [argmax]
        cs[argmax] -= 1
        while sum(cs) > 0:
            allowed_indices = [i for i in range(3) if i != sn[-1] and cs[i] > 0]
            worst = max([cs[i] for i in allowed_indices])
            for i in order:
                if i in allowed_indices and cs[i] == worst:
                    sn.append(i)
                    cs[i] -= 1
                    break
        return  "".join([ls[i] for i in sn])

def solve(colors):
    n = colors[0]
    r,b,y = colors[1], colors[5], colors[3]
    o, g, v = colors[2], colors[4], colors[6]
    if y == v and y + v == n:
        return 'YV' * (n/2)
    elif g == r and g + r == n:
        return 'GR' * (n/2)
    elif b == o and b + o == n:
        return 'BO' * (n/2)
    elif ((r <= g) and (g > 0)) or ((b <= o) and (o > 0)) or ((y <= v) and (v > 0)):
        return 'IMPOSSIBLE'
    else:
        new_colors = [n - (o + g + v),
                      r - g,
                      0,
                      y - v,
                      0,
                      b - o,
                      0]
        small_sol = solve_small(new_colors)
        if small_sol == 'IMPOSSIBLE':
            return 'IMPOSSIBLE'
        else:
            clist = list(small_sol)
            if v > 0:
                y_ind = clist.index('Y')
                clist[y_ind] = 'YV' * v + 'Y'

            if g > 0:
                r_ind = clist.index('R')
                clist[r_ind] = 'RG' * g + 'R'
            
            if o > 0:
                b_ind = clist.index('B')
                clist[b_ind] = 'BO' * o + 'B'
            return "".join(clist)
            

PATH = "/mnt/c/Users/mannes/Downloads/B-large (1).in"
#PATH = "test.in"
f = open(PATH, "r")
lines = f.readlines()

instances = [l.strip() for l in lines[1:]]
inum = 0

for i in instances:
    colors =  map(int, i.split())
    print "Case #{}: {}".format(inum + 1, solve(colors))
    inum += 1
