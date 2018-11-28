import traceback

def water_direction_map(height,width):
    return [[ 'O' for i in range (width) ] for j in range(height)]

def prepare_map(f,height,width):
    m = []
    for i in range(height):
        m.append(map(int,f.readline().strip().split()))
    return m

def eval_water_direction(m,x,y,width,height):

    n_x = x
    n_y = y-1
    e_x = x+1
    e_y = y
    w_x = x-1
    w_y = y
    s_x = x
    s_y = y+1

    n = e = w = s = True

    if n_y < 0:
        n = False
    if s_y >= height:
        s = False
    if w_x < 0:
        w = False
    if e_x >= width:
        e = False
    d = 'K' #sink
    int_d = 10000000
    if n and m[y][x] >  m[n_y][n_x] and m[n_y][n_x] <  int_d:
            int_d = m[n_y][n_x]
            d = 'N'
    if w and m[y][x] >  m[w_y][w_x] and m[w_y][w_x] <  int_d:
            int_d = m[w_y][w_x]
            d = 'W'
    if e and m[y][x] >  m[e_y][e_x] and m[e_y][e_x] <  int_d:
            int_d = m[e_y][e_x]
            d = 'E'
    if s and m[y][x] >  m[s_y][s_x] and m[s_y][s_x] <  int_d:
            int_d = m[s_y][s_x]
            d = 'S'

    return d

def add_from_k(m,x,y,a):
    n_x = x
    n_y = y-1
    e_x = x+1
    e_y = y
    w_x = x-1
    w_y = y
    s_x = x
    s_y = y+1

    n = e = w = s = True

    if n_y < 0:
        n = False
    if s_y >= height:
        s = False
    if w_x < 0:
        w = False
    if e_x >= width:
        e = False

    m[y][x] = a
    if n and m[n_y][n_x] == 'S':
        add_from_k(m,n_x,n_y,a)
    if s and m[s_y][s_x] == 'N':
        add_from_k(m,s_x,s_y,a)
    if e and m[e_y][e_x] == 'W':
        add_from_k(m,e_x,e_y,a)
    if w and m[w_y][w_x] == 'E':
        add_from_k(m,w_x,w_y,a)

def add_region(m,x,y,a):

    def add2(m,n,e,w,s,n_x,n_y,e_x,e_y,w_x,w_y,s_x,s_y,a):
        if n and m[n_y][n_x] == 'S':
            m[y][x] = a
            add_region(m,n_x,n_y,a)
        if s and m[s_y][s_x] == 'N':
            m[y][x] = a
            add_region(m,s_x,s_y,a)
        if e and m[e_y][e_x] == 'W':
            m[y][x] = a
            add_region(m,e_x,e_y,a)
        if w and m[w_y][w_x] == 'E':
            m[y][x] = a
            add_region(m,w_x,w_y,a)

    n_x = x
    n_y = y-1
    e_x = x+1
    e_y = y
    w_x = x-1
    w_y = y
    s_x = x
    s_y = y+1

    n = e = w = s = True

    if n_y < 0:
        n = False
    if s_y >= height:
        s = False
    if w_x < 0:
        w = False
    if e_x >= width:
        e = False

    if m[y][x] == 'K':
        m[y][x] = a
        add2(m,n,e,w,s,n_x,n_y,e_x,e_y,w_x,w_y,s_x,s_y,a)
        #add_from_k(m,x,y,a)
    else:

        if n and m[y][x] == 'N':
            m[y][x] = a
            add_region(m,n_x,n_y,a)
        elif s and m[y][x] == 'S':
            m[y][x] = a
            add_region(m,s_x,s_y,a)
        elif e and m[y][x] == 'E':
            m[y][x] = a
            add_region(m,e_x,e_y,a)
        elif w and m[y][x] == 'W':
            m[y][x] = a
            add_region(m,w_x,w_y,a)

        add2(m,n,e,w,s,n_x,n_y,e_x,e_y,w_x,w_y,s_x,s_y,a)


if __name__ == '__main__':
    try:
        #f = open('A-large.in')
        #w = open('A-large.out','w')
        f = open('B-large.in')
        w = open('B-large.out','w')

        n_case = int(f.readline().strip())

        for i in range(1,n_case+1):

            alphabet = map(chr,range(97,97+26))
            alphabet.reverse()
            height,width = map(int,f.readline().strip().split())
            landmap = prepare_map(f,height,width)
            wd_map = water_direction_map(height,width)
            """
            for row in landmap:
                print row
            """

            for y in range(height):
                for x in range(width):
                    wd_map[y][x] = eval_water_direction(landmap,x,y,width,height)
            """
            print '='*10 + 'case ' + str(i) + '='*10
            for row in wd_map:
                print row
            print '='*30
            """

            for y in range(height):
                for x in range(width):
                    if wd_map[y][x] in ['N','E','W','S','K']:
                        a = alphabet.pop()
                        add_region(wd_map,x,y,a)
                    #print 'wd',wd_map
            """
            print '='*10 + 'case ' + str(i) + ' ans' + '='*10
            for row in wd_map:
                print row
            print '='*30
            """

            w.write('Case #' + str(i) +':\n')
            for j in range(len(wd_map)):
                s = reduce(lambda x,y:x + ' '+ y,wd_map[j])
                if i == n_case and j == len(wd_map)-1:
                    w.write(s)
                else:
                    w.write(s + '\n')

        f.close()
        w.close()
    except :
        traceback.print_exc()
        f.close()
        w.close()
