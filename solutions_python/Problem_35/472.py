#! /usr/bin/python
import sys, string;
input = sys.argv[1];

fp = open(input, "r");

case_num = int(fp.readline().rstrip());

change = ((-1,0),(0,-1),(0,1),(1,0));
chars = "abcdefghijklmnopqrstuvwxyz";
for case in range(case_num):
    [height, width] = fp.readline().split();
    width = int(width);
    height = int(height);
    map = [];
    basin = [];
    for i in range(height):
        map.append(fp.readline().split());
        basin.append([0]*width);
    #print map, map[height - 1][width - 1];




    basin_num = 0;
    #print basin;
    for i in range(height):
        for j in range(width):
            if basin[i][j] != 0:
                continue;
            x = i;
            y = j;
            #print "x = %d, y = %d" % (x,y);
            path = [(x,y)];
            while True:
                min = map[x][y];
                min_pos = [x , y];

                for k in range(4):
                    h = change[k][0];
                    w = change[k][1];
                    
                    tmpx = x + h;
                    tmpy = y + w;
                    if tmpx < 0 or tmpx >= height or tmpy < 0 or tmpy >= width:
                        continue;

                    
                    key = map[tmpx][tmpy];
                    if key < min:
                        min = key;
                        min_pos = [tmpx, tmpy]; 
                
                #print "min_pos:(%d,%d)" % (min_pos[0], min_pos[1]);

                if basin[min_pos[0]][min_pos[1]] != 0:
                    char = basin[min_pos[0]][min_pos[1]];
                    break;
                elif [x, y] == min_pos:
                    char = chars[basin_num];
                    basin_num = basin_num + 1;
                    #path.append((min_pos[0],min_pos[1]));
                    break;
                else:
                    [x, y] = min_pos;
                    path.append((min_pos[0],min_pos[1]));
            #print path, char;
            #print basin;
            for pos in path:
                basin[pos[0]][pos[1]] = char;
            #print basin;
                        
    print "Case #%d:" % (case + 1);
    for i in range(height):
        for j in range(width):
            print basin[i][j],
        print;

fp.close();
