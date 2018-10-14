#-*-coding:utf-8-*-

import sys, copy
fh=open(sys.argv[1])
T=int(fh.readline())

def set_sinks(lat, sinks):
    H, W = len(lat), len(lat[0])
    sink_num = 0
    for i in range(H):
        up = max(0,i - 1)
        down = min(H-1, i + 1)
        for j in range(W):
            cell = lat[i][j]
            left = max(0,j-1)
            right = min(W - 1, j +1)
            c0 = lat[up][j]
            c1 = lat[i][left]
            c2 = lat[i][right]
            c3 = lat[down][j]
            if cell <= c0 and cell <= c1 and cell <= c2 and cell <= c3:
                sinks[i][j] = sink_num
                sink_num += 1
                pass
            pass
        pass
    return sink_num

def propagate(lat, sinks, marks, row, column):
    H, W = len(lat), len(lat[0])
    max_loop = H * W
    i, j = row, column
    points = []
    while True:
        if sinks[i][j] is not None:
            for r,c in points:
                marks[r][c] = sinks[i][j]
                pass
            break
        points.append((i,j))
        l = lat[i][j]
        up = max( 0, i - 1)
        down = min( H - 1, i + 1)
        left = max( 0, j - 1)
        right = min(W - 1, j + 1)
        north = lat[up][j]
        west  = lat[i][left]
        east  = lat[i][right]
        south = lat[down][j]
        if north < l and (north <= west and north <= east and north <= south):
            i -= 1
        elif west < l and (west <= east and west <= south):
            j -= 1
        elif east < l and (east <= south):
            j += 1
        elif south < l:
            i += 1
        else:
            print(row, column, i,j)
            print(l, cu, cl, cr, cd)
            raise Exception('no flow')
            pass
        pass
    pass

def output(pat):
    for row in pat:
        line = ''
        for c in row:
            if c is None: 
                line += ' . '
            else:
                line += '{0:2d} '.format(c)
                pass
            pass
        print(line)
        pass
    pass

def convert_to_alphabet(marks):
    basins = {}
    cc = 97
    for row in marks:
        line = ''
        for cell in row:
            if cell not in basins:
                basins[cell] = chr(cc)
                cc += 1
                pass
            if line != '': line += ' '
            line += basins[cell]
            pass
        print(line)
    pass


for num_cases in range(T):
    H,W=map(int,fh.readline().split(' '))
    lat = []
    marks = []
    sinks = []
    for i in range(H):
        lat.append(map(int,fh.readline().split(' ')))
        sinks.append([None] * W)
        pass
    set_sinks(lat, sinks)
    marks = copy.deepcopy(sinks)
    #output(lat)
    #print('')
    #output(sinks)
    #print('')
    print("Case #{0}:".format(num_cases + 1))
    for i in range(H):
        for j in range(W):
            if marks[i][j] is not None: continue
            try:
                propagate(lat, sinks, marks, i, j)
            except:
                print(i, j)
                output(lat)
                output(sinks)
                output(marks)
                raise
            pass
        pass
    convert_to_alphabet(marks)
    #print('')
    pass
