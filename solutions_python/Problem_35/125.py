#!/usr/bin/python
import sys

directions = [(-1,0), (0,-1), (0,1), (1,0)]

def dir_is_valid(x,y, max_x, max_y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y

class Cell(object):
    def __init__(self):
        self.ptr = None

def calc_ans(hmap):
    point_map = []
    for row in hmap:
        point_map.append([])
        for col in row:
            point_map[-1].append(Cell())

    for x in xrange(len(hmap)):
        for y in xrange(len(hmap[x])):
            best_x = x
            best_y = y
            best_dir = None
            for dir in directions:
                x_new = x + dir[0]
                y_new = y + dir[1]
                if not dir_is_valid(x_new, y_new, len(hmap), len(hmap[x])):
                    continue
                if hmap[best_x][best_y] > hmap[x_new][y_new]:
                    best_x = x_new
                    best_y = y_new
                    best_dir = point_map[best_x][best_y]
            point_map[x][y].ptr = best_dir

    curr_let = ord('a')-1
    for x in xrange(len(hmap)):
        for y in xrange(len(hmap[x])):
            curr_pos = point_map[x][y]
            while(curr_pos.ptr.__class__==Cell):
                curr_pos = curr_pos.ptr
            if curr_pos.ptr is None:
                curr_let += 1
                curr_pos.ptr = curr_let
            new_let = curr_pos.ptr
            curr_pos = point_map[x][y]
            while(curr_pos.ptr.__class__==Cell):
                next_pos = curr_pos.ptr
                curr_pos.ptr = new_let
                curr_pos = next_pos

    return "\n".join([" ".join([chr(cell.ptr) for cell in row]) for row in point_map])

def main():
    handle = file(sys.argv[1])
    T = int(handle.readline())
    for case_no in range(1,T+1):
        H,W = map(lambda x: int(x), handle.readline().split())
        hights_map = []
        for i in range(H):
            hights_map.append(map(lambda x: int(x), handle.readline().split()))

        print "Case #%d:\n%s" % (case_no, calc_ans(hights_map))

main()
