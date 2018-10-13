f = open('Alarge.in','r')
a = f.read()
b = a.split('\n')
del(b[-1])
f.close()


def solve(l):
    pos = {}
    pos['X'] = []
    pos['O'] = []
    pos['T'] = None
    for i in xrange(len(l)):
        for j in xrange(len(l[0])):
            if l[i][j] == 'T':
                pos['T'] = (i,j)

            elif l[i][j] == 'X':
                pos['X'].append((i,j))
            elif l[i][j] == 'O':
                pos['O'].append((i,j))

    ## Check Row.
    #for i in xrange(4):
    #    for j in xrange(4):

    count = 0

    while count < 4:
        a = []
        for i in xrange(4):
            a = a + [l[count][i]]
        m = same(a)

        if m != None:
            if m[0] == True:
                return m[1] + ' won'
        count += 1

    ## Check Column.

    count = 0
    while count < 4:
        a = []
        for i in xrange(4):
            a = a + [l[i][count]]
        #print a
        m = same(a)

        if m != None:
            if m[0] == True:
                return m[1] + ' won'
        count += 1

    ## Check Diagonal.

    ## First diagonal...
    partial = [l[i][i] for i in xrange(4)]
    m = same(partial)
    if m != None:
        if m[0] == True:
            return m[1] + ' won'

    ## Second diagonal...

    p = [l[i][j] for i in xrange(4) for j in xrange(4) if i + j == 3]
    m = same(p)
    if m != None:
        if m[0] == True:
            return m[1] + ' won'
    """
    else:
        ## then its either draw or game not yet completed.
        for i in xrange(len(l)):
            for j in xrange(len(l[0])):
                if l[i][j] == '.':
                    return 'Game has not completed'

        return 'Draw'

    """
    for i in xrange(len(l)):
        for j in xrange(len(l[0])):
            if l[i][j] == '.':
                return 'Game has not completed'

    return 'Draw'
    

    
def same(partial_list):
    q = partial_list
    symbol = q[0]
    #########################
    if symbol == 'T':
        a = q[1]
        if a != '.':
            for i in xrange(2,len(q)):
                if q[i] != a:
                    return False, -1

            return True, a
    #########################

    
    elif symbol != '.':
        pos = -1
        ## symbol is either 'X' or 'O'....
        c = False

        for i in xrange(len(q)):
            if q[i] == 'T':
                c = True
                pos = i

        if c == False:
            ## i.e. there is no 'T' in q
            for i in xrange(len(q)):
                if q[i] != symbol:
                    return False, -1
            return True, q[0]

        else: ## c == True, i.e. there is a 'T' in q
            for i in xrange(len(q)):
                if i != pos and q[i] != symbol:
                    return False, -1

            return True,q[0]
    ##########################


T = int(b[0])
j = 1
    

g = open('AlargeOut','w')

for i in xrange(T):
    x = b[5*i+1:5*i + 5]
    s = solve(x)
    w = 'Case #%d: %s \n' % (j,s)
    g.write(w)
    j += 1

g.close()
