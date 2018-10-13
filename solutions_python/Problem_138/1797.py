
def war(naomi, ken) :
    ken2 = list(ken)
    win = 0
    for val in naomi :
        for i in range( len(ken2) ) :
            if ken2[i] > val :
                ken2.pop(i)
                val = -1
                break
        if val >= 0:
            win += 1
            ken2.pop(0)
    return win

def deceitful(naomi, ken) :
    naomi2 = list(naomi)
    ken2 = list(ken)
    win = 0
    while len(naomi2) > 0 :
        if naomi2[-1] > ken2[-1] :
            win += 1
            naomi2.pop(-1)
            ken2.pop(-1)
        else :
            naomi2.pop(0)
            ken2.pop(-1)
    return win
        
def solve(f) :
    n = int(f.readline())
    naomi = f.readline().split()
    naomi = [ float(f) for f in naomi ]
    naomi.sort()

    ken = f.readline().split()
    ken = [ float(f) for f in ken ]
    ken.sort()

    
    

    return deceitful(naomi, ken), war(naomi, ken)

if __name__ == '__main__' :
    with open('D-small-attempt0.in') as f:
        t = int(f.readline())
        for i in range(t) :
            print ('Case #{0}: {1[0]} {1[1]}'.format(i + 1, solve(f)))
