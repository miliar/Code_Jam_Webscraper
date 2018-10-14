import math

def arch(R, d):
    if d >= R:
        return 0
    return math.acos(d/R)*R**2- math.sqrt(R**2-d**2)*d

def string(R, d1, d2):
    '''d2 > d1'''
    if d2 > R:
        return arch(R, d1)
    else:
        return arch(R, d1) - arch(R, d2)

def times4(R, left, right, up, down):
    if right >= R or down >= R:
        return 0
    tmp = math.sqrt(R**2 - right**2)
    if tmp < up:
        up = tmp
    tmp = math.sqrt(R**2 - down**2)
    if tmp < left:
        left = tmp
    arch_left = arch(R, left)/2
    arch_up = arch(R, up)/2
    square_down = down*(left-right)
    square_right = right*(up-down)
    square = right*down
    return math.pi*R**2/4 - arch_left - arch_up - square_down - square_right - square


def through(f, R, t, r, g):
    RR = R-t-f
    if 2*f > g:
        return 0

    string_loc = [0]
    d = 0
    s_no = 0
    while string_loc[-1]+3*r+g < R-t:
        d += (2*r + g)
        string_loc.append(d)
        tmp = math.sqrt((R-t)**2-d**2)
        s_no += int(tmp/(g+2*r))*4

    d += (2*r + g)
    string_loc.append(d)

    x4 = 0
    for i in xrange(1, len(string_loc)):
        loc = string_loc[i]
        if loc > R-t:
            square_no = 0
        else:
            tmp = math.sqrt((R-t)**2-loc**2)
            square_no = int(tmp/(g+2*r))
        last = string_loc[i-1]
        if last > R-t:
            last_square_no = 0
        else:
            tmp = math.sqrt((R-t)**2-last**2)
            last_square_no = int(tmp/(g+2*r))
        up = loc - f - r if loc < R-t else loc
        down = last + f + r
        for j in xrange(square_no, last_square_no+1):
            left = string_loc[j+1]
            left = left - f -r if left < R-t else left
            right = string_loc[j] + f + r
            x4 += times4(RR, left, right, up ,down)

    s = s_no * (g-2*f)**2

    return s+x4*4


if __name__ == '__main__':
    import sys
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    wfile = open(out_file, 'w')
    case_no = 1
    for line in open(in_file):
        if len(line.strip().split()) != 5:
            continue
        f, R, t, r, g = line.strip().split()
        R = float(R)
        t = float(t)
        g = float(g)
        r = float(r)
        f = float(f)
        p = through(f, R, t, r, g)/math.pi/(R)**2
        wfile.write('Case #'+str(case_no)+': '+str(1-p)+'\n')
        case_no += 1








#END