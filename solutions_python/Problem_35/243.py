route = [(0,-1), (-1,0), (1,0), (0,1)]

def build_direction(_map):
    _dm = [[-1 for c in r] for r in _map]
    w = len(_map[0])
    h = len(_map)
    for y in range(h):
        for x in range(w):
            cv = _map[y][x]
            ns = [(i, (x+p[0], y+p[1])) for i, p in enumerate(route)]
            vs = [(i, _map[_y][_x]) for (i, (_x,_y)) in ns if 0<=_x<w and 0<=_y<h]

            _min = None
            for v in vs:
                if _min==None or v[1]<_min[1]:
                    _min = v
                    
            if _min is not None and cv>_min[1]:
                _dm[y][x] = _min[0]
            else:
                _dm[y][x] = None    
    return _dm

def getLabel(ps, _dir, _label):
    r = _dir[ps[1]][ps[0]]
    current_label = _label[ps[1]][ps[0]]
    if current_label is not None or r==None:
        return current_label
    else:
        nr = route[r]
        return getLabel((ps[0]+nr[0], ps[1]+nr[1]), _dir, _label)

def markPath(mark, ps, _dir, _label):
    _label[ps[1]][ps[0]] = mark
    r = _dir[ps[1]][ps[0]]
    if r is not None:
        nr = route[r]
        markPath(mark, (ps[0]+nr[0], ps[1]+nr[1]), _dir, _label)

def solve(_map):
    _dir = build_direction(_map)
    _label = [[None for c in r] for r in _map]

    w = len(_map[0])
    h = len(_map)
    lbl = 0
    for y in range(h):
        for x in range(w):
            if _label[y][x]==None:
                tlbl = getLabel((x,y), _dir, _label)
                if tlbl==None:
                    markPath(lbl, (x,y), _dir, _label)
                    lbl=lbl+1
                else:
                    markPath(tlbl, (x,y), _dir, _label)
    return _label
    

fin = open('B-large.in', 'r')
fout = open('out.txt', 'w')
N = int(fin.readline())
for i in range(1, N+1):
    M = [int(x) for x in fin.readline().split()]
    _map = []
    for j in range(M[0]):
        _map.append([int(x) for x in fin.readline().split()])

    label = solve(_map)
    fout.write('Case #%i:\n'%i)
    for r in label:
        fout.write(' '.join([chr(97+c) for c in r]) + '\n')
        
fin.close()
fout.close()
    
    
