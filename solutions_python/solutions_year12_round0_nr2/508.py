'''
Created on Apr 14, 2012

@author: silent
'''
import sys

point_map_normal = {}
point_map_suprising = {}

def get_input(input_file):
    infile = open(input_file)
    return infile

def get_output(output_file):
    outfile = open(output_file, "w")
    return outfile

def init():
    for a in range(10, -1, -1):
        for b in range(a+2, a-1, -1):
            if b > 10:
                continue
            for c in range(a+2, b-1, -1):
                if c > 10:
                    continue
                sum_point = a + b + c
                if sum_point in point_map_normal.keys():
                    point_map_suprising[sum_point] = (c, b, a)
                else:
                    point_map_normal[sum_point] = (c, b, a)

def has_ge_point(points, min_point):
    for point in points:
        if point >= min_point:
            return True
    return False


def find_max_googler(googlers, suprising, min_point, total_points):
    total_points.sort(reverse=True)
    suprising_count = 0
    result = 0

    for total in total_points:
        if total > ((min_point-1)*3) or total > 28 or total < 2:
            points = point_map_normal[total]
        elif suprising_count < suprising:
            points = point_map_suprising[total]
            suprising_count = suprising_count + 1
        else:
            points = point_map_normal[total]
        
        if has_ge_point(points, min_point):
            result = result + 1
    return result

if __name__ == '__main__':
    if len(sys.argv) == 1:
        input_file = 'input.in'
    else:
        input_file = sys.argv[1]
    filename = input_file.split(".")[0]
    infile = get_input(input_file)
    outfile = get_output(filename + ".out")
    
    init()
    
    t = int(infile.readline())
    
    for case_num in range(t):
        total_points = map(int, infile.readline().split())
        googlers = total_points.pop(0)
        suprising = total_points.pop(0)
        min_point = total_points.pop(0)
        
        result = find_max_googler(googlers, suprising, min_point, total_points)
        
        outfile.write("Case #%d: %s\n" % (case_num+1, result))
        print "Case #%d: %s" % (case_num+1, result)
    
    infile.close()
    outfile.close()
