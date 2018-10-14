xwon="X won"
owon="O won"
draw="Draw"
nocomplete="Game has not completed"
mix="mix"

def check_row(a):
    s = set(a)

    if '.' in s:
        return mix;
    
    length = len(s)
    if length > 2:
        return mix
    elif length == 1:
        if 'X' in s:
            return xwon;
        elif 'O' in s:
            return owon;
    elif length == 2:
        if 'X' in s and 'T' in s:
            return xwon;
        elif 'O' in s and 'T' in s:
            return owon;
    return mix
        
def check_col(twomap, col):
    l = []
    for i in range(4):
        l.append(twomap[i][col]);
    return check_row(l);

def check_cross(twomap):
    order = range(4)
    l = []
    for i in order:
        l.append(twomap[i][i])
    
    return check_row(l)

def check_cross_up(twomap):
     order = range(4)
     order2 = [3,2,1,0]
     l = []

     for i in order:
        l.append(twomap[i][order2[i]])

     return check_row(l);
        

def check_finish(twomap):
    for i in range(4):
        if '.' in twomap[i]:
            return False;
    return True

def checkttt(twomap, height):
    
    for row in range(4):
        r = check_row(twomap[row])
        if r == xwon or r == owon:
            return r

    for col in range(4):
        r = check_col(twomap, col)
        if r == xwon or r == owon:
            return r
    

    r = check_cross(twomap);
    if r == xwon or r == owon:
        return r;
    r = check_cross_up(twomap);
    if r == xwon or r == owon:
        return r;

    finish = check_finish(twomap);
    if finish:
        return draw;
    else:
        return nocomplete

# Pass the deal function.
def googleJamReadCase(filename, func):
    with open(filename) as f:
        casenum = int(f.readline())

        for casei in range(casenum):
            twomap = []
            height = 4
            
            for i in range(height):
                a = list(f.readline().strip('\n'));
                twomap.append(a)

            result = func(twomap, height)
            print "Case #%d: %s" % (casei + 1, result)
            f.readline()
                    
                    
                

if __name__ == '__main__':
    import sys
    googleJamReadCase(sys.argv[1], checkttt)
