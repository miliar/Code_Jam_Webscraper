def pt_val(l, point):
    return l[point[0]][point[1]]

def mark(l, p, ch):
    #print('mark: ' + str(p[0]) + ", " +str(p[1]) + ' with: ' + ch)
    try:
        int(l[p[0]][p[1]])
        l[p[0]][p[1]] = ch
        return 1
    except:
        for i in range(1, len(labels)-1):
            for j in range(1, len(labels[i])-1):
                curr = (i, j)
                if pt_val(l, curr) == ch:
                    l[curr[0]][curr[1]] = l[p[0]][p[1]]
    return 0

def find_max(labels):
    curr_max = (0, 0)
    for i in range(1, len(labels)-1):
        for j in range(1, len(labels[i])-1):
            curr = (i, j)
            try:
                int(pt_val(labels, curr))
                if pt_val(labels, curr) > pt_val(labels, curr_max):
                    curr_max = (i, j)
            except:
                pass

    if pt_val(labels, curr_max) > -1:
        return curr_max
    else:
        return -1

def choose_next(map, point, vis):
    #print('next-for: ' + str(point[0]) + ", " +str(point[1]))
    pts =   [
                (0,0),
                (point[0]-1, point[1]),
                (point[0], point[1]-1),
                (point[0], point[1]+1),
                (point[0]+1, point[1])
            ]
    curr_next_ind = 0

    for p in range(1, len(pts)):
        #print('t-p: ' + str(pts[p][0]) + ", " +str(pts[p][1]))
        #print( str(pt_val(map, pts[p])) + ' vs. ' + str(pt_val(map, pts[curr_next_ind])) )
        try:
            vis.index(pts[p])
        except:
            if pt_val(map, pts[p]) < pt_val(map, pts[curr_next_ind]) and pt_val(map, pts[p]) < pt_val(map, point):
                curr_next_ind = p

    if curr_next_ind == 0:
        #print('No next?!')
        return -1
    else:
        #print('n-c: ' + str(curr_next_ind))
        return pts[curr_next_ind]

if __name__ == '__main__':
    fin = open("./test.in", "r")
    fout = open("./test.out", "w")

    line = fin.readline()
    N = int(line)

    for test in range(0, N):
        total = 0
        line = fin.readline().split(" ")
        height = int(line[0]) + 2
        width = int(line[1]) + 2

        map = []
        labels = []
        res = []

        for h in range(0, height):
            row = []
            row2 = []
            row3 = []
            for w in range(0, width):
                row.append(999999)
                row2.append(-999999)
                row3.append(0)
            map.append(row)
            labels.append(row2)
            res.append(row3)

        for h in range(1, height-1):
            tmp = fin.readline().split(" ")
            for w in range(1, width-1):
                map[h][w] = int(tmp[w-1])
                labels[h][w] = int(tmp[w-1])

        ch = 'a'
        while 1:
            vis = []
            max = find_max(labels)
            if max == -1: break
            mark(labels, max, ch)

            q = 1
            while 1:
                vis.append(max)
                next = choose_next(map, max, vis)
                if next == -1: break
                q = mark(labels, next, ch)
                max = next
            ch = chr(ord(ch) + q)

        u = []
        z = []
        i = 0
        for i in range(ord('a'), ord('z') + 1):
            u.append(chr(i))

        for h in range(1, height-1):
            for w in range(1, width-1):
                try:
                    z.index(labels[h][w])
                except:
                    z.append(labels[h][w])

        for h in range(1, height-1):
            for w in range(1, width-1):
                res[h][w] = u[z.index(labels[h][w])]

        for h in range(1, height-1):
            print(res[h])

        fout.write("Case #" + str(test+1) + ":\n")
        for h in range(1, height-1):
            for w in range(1, width-1):
                fout.write(res[h][w])
                if w < width-2: fout.write(" ")
            fout.write("\n")