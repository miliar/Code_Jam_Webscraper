import itertools

mirror1 = {'d':'l', 'l':'d', 'u':'r', 'r':'u'}
mirror2 = {'u':'l', 'l':'u', 'd':'r', 'r':'d'}
qwerty = {0:'|', 1:'-'}

def extend(map, i, j, d):
    r = len(map)
    c = len(map[0])
    if d == 'u':
        i -= 1
    if d == 'd':
        i += 1
    if d == 'l':
        j -= 1
    if d == 'r':
        j += 1
    if i < 0 or i >= r or j < 0 or j >= c:
        return i, j, None
    q = map[i][j]
    if q == '.':
        return i, j, d
    if q == '\\':
        d = mirror2[d]
        return i, j, d
    if q == '/':
        d = mirror1[d]
        return i, j, d
    if q == '#':
        return i, j, None
    if q in ['|','-']:
        return i, j, 'boom'

def solve(empty, covers, map, bs):
    if (None, None) in covers:
        return "IMPOSSIBLE"
    dirs = [0 for c in covers]
    opts = []
    for c in covers:
        if c[0] == None:
            opts.append((1,))
        if c[1] == None:
            opts.append((0,))
        if None not in c:
            opts.append((1,0))

    for i in empty:
        found = False
        for c in covers:
            if c[0] is not None:
                if i in c[0]:
                    found = True
                    break
            if c[1] is not None:
                if i in c[1]:
                    found = True
                    break
        if found == False:
            return "IMPOSSIBLE"

    for i in itertools.product(*opts):
        covered = set()
        for j, d in enumerate(i):
            covered = covered | covers[j][d]
        if len(covered) == len(empty):
            
            replaces = [qwerty[q] for q in i]
            for ind, loc in enumerate(bs):
                (x,y) = loc
                sub = map[x]
                sub = list(sub)
                sub[y] = replaces[ind]
                sub = ''.join(sub)
                map[x] = sub
            for k in range(r):
                print map[k]
            return "POSSIBLE\n" + '\n'.join(map)
            #DO THE POST-PROCESSING

    return "IMPOSSIBLE"
    
        
                
            

fout = open('out.txt','w')
with open('in.txt') as f:
    T = int(f.readline())
    for case in range(1,T+1):
        line = f.readline()

        line = line.split()
        r = int(line[0])
        c = int(line[1])

        map = []
        for i in range(r):
            map.append(f.readline().strip())

        empty = []
        bs = []
        for i in range(r):
            for j in range(c):
                q = map[i][j]
                if q == '.':
                    empty.append((i,j))
                if q in ['|','-']:
                    bs.append((i,j))

        covers = []
        for index in range(len(bs)):
            #up
            (i,j) = bs[index]
            history = []
            code = 'u'
            valid = True
            ud = set()
            while True:
                i, j, code = extend(map, i, j, code)
                if (i, j, code) in history:
                    break
                else:
                    history.append((i,j,code))
                if code == None:
                    break
                if code == 'boom':
                    valid = False
                    break
                if map[i][j] == '.':
                    ud.add((i,j))
            #down
            (i,j) = bs[index]
            history = []
            code = 'd'
            if valid:
                while True:
                    i, j, code = extend(map, i, j, code)
                    if (i, j, code) in history:
                        break
                    else:
                        history.append((i,j,code))
                    if code == None:
                        break
                    if code == 'boom':
                        valid = False
                        break
                    if map[i][j] == '.':
                        ud.add((i,j))
            if not valid:
                ud = None

            #left
            (i,j) = bs[index]
            history = []
            code = 'l'
            valid = True
            lr = set()
            while True:
                i, j, code = extend(map, i, j, code)
                if (i, j, code) in history:
                    break
                else:
                    history.append((i,j,code))
                if code == None:
                    break
                if code == 'boom':
                    valid = False
                    break
                if map[i][j] == '.':
                    lr.add((i,j))
            #right
            (i,j) = bs[index]
            history = []
            code = 'r'
            if valid:
                while True:
                    i, j, code = extend(map, i, j, code)
                    if (i, j, code) in history:
                        break
                    else:
                        history.append((i,j,code))
                    if code == None:
                        break
                    if code == 'boom':
                        valid = False
                        break
                    if map[i][j] == '.':
                        lr.add((i,j))
            if not valid:
                lr = None

            covers.append((ud, lr))
            if (ud,lr) == (None, None):
                pass
                #break


        
        
        ans = solve(empty, covers, map, bs)
        
        str = "Case #%d: %s\n" % (case, ans)
        print str,
        fout.write(str)
fout.close()
