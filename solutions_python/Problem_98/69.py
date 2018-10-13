num = raw_input()

for i in range(int(num)):
    line = raw_input()
    sh,sw,sd = line.split(" ")
    h = int(sh)
    w = int(sw)
    d = int(sd)
    map_orig = []
    map_width = w-2
    map_height = h-2
    
    # get original map
    for j in range(h):
        line = raw_input()
        if j==0 or j==h-1:
            1
        else:
            needed = line[1:w-1]
            for char in needed:
                map_orig.append(char)


    # mirroring
    map2 = []
    map3 = []
    map4 = []
    for j in range(map_height):
        for k in range(map_width):
            map2.append(map_orig[j*map_width+(map_width-1-k)])
            map3.append(map_orig[(map_height-1-j)*map_width+k])
            map4.append(map_orig[(map_height-1-j)*map_width+(map_width-1-k)])

    map_mirrored_width = max(d*4, map_width*4)
    map_mirrored_height = max(d*4, map_height*4)

    map_mirrored = []
    for j in range(map_mirrored_height):
        for k in range(map_mirrored_width):
            if (j // map_height) % 2 == 0:
                if (k // map_width) % 2 == 0:
                    # map 1
                    map_mirrored.append(map_orig[(j-(j//map_height)*map_height)*map_width + k-(k//map_width)*map_width])
                else:
                    # map 2
                    map_mirrored.append(map2[(j-(j//map_height)*map_height)*map_width+k-(k//map_width)*map_width])
            else:
                if (k // map_width) % 2 == 0:
                    # map 3
                    map_mirrored.append(map3[(j-(j//map_height)*map_height)*map_width+k-(k//map_width)*map_width])
                else:
                    # map 4
                    map_mirrored.append(map4[(j-(j//map_height)*map_height)*map_width+k-(k//map_width)*map_width])
    #for j in range(map_mirrored_height):
    #    for k in range(map_mirrored_width):
    #        print map_mirrored[j*map_mirrored_width+k],
    #    print ""

    # decide center
    min_dist = 99999
    for j in range(map_mirrored_height):
        for k in range(map_mirrored_width):
            if map_mirrored[j*map_mirrored_width+k] == "X":
                dist = (j-map_mirrored_width/2)*(j-map_mirrored_width/2)+(k-map_mirrored_height/2)*(k-map_mirrored_height/2)
                if min_dist > dist:
                    x0 = j
                    y0 = k
                    min_dist = dist

    point_array = []
    for j in range(map_mirrored_height):
        for k in range(map_mirrored_width):
            if map_mirrored[j*map_mirrored_width+k] == "X":
                dist = (j-x0)*(j-x0)+(k-y0)*(k-y0)
                if dist > 0 and dist <= d*d:
                    point = (j-x0), (k-y0)
                    if len(point_array) == 0:
                        point_array.append(point)
                    else:
                        flag=1
                        for appended_point in point_array:
                            if point[1]*appended_point[0] == appended_point[1]*point[0]:
                                if (point[1]*appended_point[1] >= 0 and point[0]*appended_point[0] >= 0):
                                    flag=0
                                    break
                        if flag:
                            point_array.append(point)
    #print point_array
    print "Case #" + str(i+1) + ": " + str(len(point_array))
