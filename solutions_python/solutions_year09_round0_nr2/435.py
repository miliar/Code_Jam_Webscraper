lower_list = [chr(i) for i in xrange(ord('a'), ord('z') + 1)]
big = 20000
for test_case in xrange(input()):
    h, w = [int(x) for x in raw_input().split()]
    #print h, w

    # read map
    map = []
    min_val = -1
    for row in xrange(h):
        r = [int(x) for x in raw_input().split() ]
        new_min = min(r)
        if new_min < min:
            main = new_min
        map.append( r )

    #algorithm
    lower_count = 0
    basin_map = [ [ None for _ in xrange(w)] for _ in xrange(h) ]
    for r in xrange(h): 
        for c in xrange(w):

            if basin_map[r][c] != None:
                continue

            def get_dir(r, c):
                global map, big

                def dircmp(a,b):
                    if a[1] != b[1]:
                        if a[1] < b[1]:
                            return -1
                        else:
                            return 1
                    else:
                        if a[0] < b[0]:
                            return -1
                        else:
                            return 1

                if r > 0: 
                    north = map[r-1][c] 
                else: 
                    north = big
                if r < h-1:
                    south = map[r+1][c] 
                else:
                    south = big
                if c > 0: 
                    west = map[r][c-1] 
                else: 
                    west = big
                if c < w-1: 
                    east = map[r][c+1] 
                else: 
                    east = big

                return sorted( ((1,north), (2,west), (3, east), (4, south) ), dircmp )[0]

            def get_label( r, c ):
                global lower_count, basin_map, map
                if basin_map[r][c] != None:
                    return basin_map[r][c]
                else:
                    dir = get_dir( r, c )
                    if dir[1] >= map[r][c]:
                        result = lower_list[lower_count]
                        lower_count += 1
                        basin_map[r][c] = result
                        return result
                    else:
                        if dir[0] == 1:
                            label = get_label( r-1, c )
                        elif dir[0] == 2:
                            label = get_label( r, c-1 )
                        elif dir[0] == 3:
                            label = get_label( r, c+1 )
                        else:
                            label = get_label( r+1, c)
                        
                        basin_map[r][c] = label
                        return label
            
            basin_map[r][c] = get_label(r,c)

    #print ">>>> basin_map:", basin_map
    print "Case #%d:" % (test_case+1)
    for h_count in xrange(h):
        print " ".join(basin_map[h_count])


            #print "*" , north, south, west, east
    #        dir = get_dir( r, c )
    #        #dir = sorted( ((1,north), (2,east), (3, west), (4, south) ), dircmp )[0]
    #        if dir[0] == 1:
    #            label = get_label( r-1, c )
    #        elif dir[0] == 2:
    #            label = get_label( r, c+1 )
    #        elif dir[0] == 3:
    #            label = get_label( r, c-1 )
    #        else:
    #            label = get_label( r+1, c)
   # 

