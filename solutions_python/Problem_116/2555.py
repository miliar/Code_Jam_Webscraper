

def read_case(b):
    for i in range(4):
        b[i] = raw_input()

def treat_case(b, case):
    ho = 0
    hx = 0
    vo = 0
    vx = 0
    p = 0

    for i in range(4):
        ho = 0
        hx = 0
        vo = 0
        vx = 0
        for j in range(4):
            hc = b[i][j]
            vc = b[j][i]
            if hc == 'T':
                ho = ho + 1
                hx = hx + 1
            elif hc == 'O':
                ho = ho + 1
            elif hc == 'X':
                hx = hx + 1
            else:
                p = p + 1
                
            if vc == 'T':
                vo = vo + 1
                vx = vx + 1
            elif vc == 'O':
                vo = vo + 1
            elif vc == 'X':
                vx = vx + 1
            else:
                p = p

        if ho == 4 or vo == 4:
            return "Case #" + str(case) + ': O won'
        if hx == 4 or vx == 4:
            return "Case #" + str(case) + ': X won'


    x1 = 0
    o1 = 0
    x2 = 0
    o2 = 0
    for i in range(4):
        c1 = b[i][i]
        c2 = b[i][3-i]
        if c1 == 'O':
            o1 = o1 + 1
        elif c1 == 'X':
            x1 = x1 + 1
        elif c1 == 'T':
            o1 = o1 + 1
            x1 = x1 + 1

        if c2 == 'O':
            o2 = o2 + 1
        elif c2 == 'X':
            x2 = x2 + 1
        elif c2 == 'T':
            o2 = o2 + 1
            x2 = x2 + 1  

    if o1 == 4 or o2 == 4:
        return "Case #" + str(case) + ': O won'
    elif x1 == 4 or x2 == 4:
        return "Case #" + str(case) + ': X won'



    elif p == 0:
        return "Case #" + str(case) + ': Draw'
    else:
        return "Case #" + str(case) + ': Game has not completed'


if __name__ == "__main__":
    b = [[] for _ in range(4)]
    cases = int(raw_input())
    for i in range(cases):
        read_case(b)
        print treat_case(b, i+1)
        _ = raw_input()
