import pprint
pp = pprint.PrettyPrinter(indent=4)

handler = open('B-small-attempt0.in.txt', 'r')
# handler = open('B-large.in.txt', 'r')
# handler = open('b.in.txt', 'r')


numcases = int(handler.readline().strip())
for i in xrange(numcases):
    names = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(' ')
    names.reverse()
    H, W = handler.readline().strip().split(' ')
    
    m = []
    for j in xrange(int(H)):
        row = handler.readline().strip().split(' ')
        d = []
        for r in row:
            d.append([int(r), None])
        m.append(d)
        
    # pp.pprint(m)
    
    for h in xrange(int(H)):
        for w in xrange(int(W)):
            coords = [h, w]
            for step in xrange(int(H)*int(W)):
                new_coords = None
                # --
                try:
                    south = m[coords[0]+1][coords[1]]
                except IndexError:
                    south = None
                
                if south and south[0]<m[coords[0]][coords[1]][0]:
                    new_coords = [coords[0]+1, coords[1]]
                # --
                try:
                    east = m[coords[0]][coords[1]+1]
                except IndexError:
                    east = None
                
                if (east and east[0]<m[coords[0]][coords[1]][0]) and ((new_coords and east[0]<=m[new_coords[0]][new_coords[1]][0]) or new_coords is None):
                    new_coords = [coords[0], coords[1]+1]
                # --
                if coords[1]==0:
                    west = None
                else:
                    west = m[coords[0]][coords[1]-1]
                if (west and west[0]<m[coords[0]][coords[1]][0]) and ((new_coords and west[0]<=m[new_coords[0]][new_coords[1]][0]) or new_coords is None):
                    new_coords = [coords[0], coords[1]-1]
                # --
                if coords[0]==0:
                    north = None
                else:
                    north = m[coords[0]-1][coords[1]]
                
                if (north and north[0]<m[coords[0]][coords[1]][0]) and ((new_coords and north[0]<=m[new_coords[0]][new_coords[1]][0]) or new_coords is None):
                    new_coords = [coords[0]-1, coords[1]]
                # --
                
                if new_coords:
                    coords = new_coords
                else:
                    if m[coords[0]][coords[1]][1] is None:
                        name = names.pop()
                        m[coords[0]][coords[1]][1] = name
                        m[h][w][1] = name
                        # print h,w, ' -> ', coords[0], coords[1], name
                        break
                    else:
                        m[h][w][1] = m[coords[0]][coords[1]][1]
                
    # pp.pprint(m)
    # break
    print "Case #%s:" % (i+1)
    for h in xrange(int(H)):
        print " ".join([f[1] for f in m[h]])

handler.close()