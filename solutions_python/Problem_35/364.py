#! /usr/bin/env python

import pprint
import sys
import string

next_letter = 0

def scan_cells(basin_map, row, col):
    if basin_map[row][col]['basin'] != None:
        return basin_map[row][col]['basin']

    flow_cell = None
    lowest_altitude = basin_map[row][col]['height']
    # test where water flows down
    # North
    if not (row - 1) < 0:
        if  basin_map[row - 1][col]['height'] < lowest_altitude:
            flow_cell = basin_map[row - 1][col]
            lowest_altitude = flow_cell['height']


    # West
    if not (col - 1 < 0):
        if basin_map[row][col - 1]['height'] < lowest_altitude:
            flow_cell = basin_map[row][col - 1]
            lowest_altitude = flow_cell['height']

                        
    # East
    if not ((col + 1) == len(basin_map[row])):
        if basin_map[row][col + 1]['height'] < lowest_altitude:
            flow_cell = basin_map[row][col + 1]
            lowest_altitude = flow_cell['height']


    # South
    if not (row + 1 == len(basin_map)):
        if basin_map[row + 1][col]['height'] < lowest_altitude:
            flow_cell = basin_map[row + 1][col]
            lowest_altitude = flow_cell['height']

    if flow_cell == None:
        global next_letter
        basin_map[row][col]['basin'] = string.ascii_letters[next_letter]
        next_letter += 1
    else:
        basin_map[row][col]['basin'] = scan_cells(basin_map, flow_cell['row'], flow_cell['col'])
        
    return basin_map[row][col]['basin']


if __name__ == "__main__":
    global next_letter
    data = open(sys.argv[1])
    
    cases = int(data.readline().strip())

    for case in range(1, cases + 1):
        next_letter = 0
        dimensions = data.readline().strip().split()

        print ("Case #%s:" % case)
        basin_map = []
        for row in range(0, int(dimensions[0])):
            basin_map.append( [ {"basin": None,
                                 "height": int(x),
                                 "row": len(basin_map),
                                 "col": col} for col, x in enumerate(data.readline().strip().split())
                              ])

        
        
        for row in range(0, int(dimensions[0])):
            print_string = ""
            for col in range(0, int(dimensions[1])):
                # See if this one has been hit by another flow
                if basin_map[row][col]['basin'] == None:
                    basin_map[row][col]['basin'] = scan_cells(basin_map, row, col)

                print_string += "%s " % basin_map[row][col]['basin']
            print (print_string.strip())
        

                

        
                                                                
