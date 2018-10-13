from sys import stdout, stderr, stdin
import math

def read_line():
    return stdin.readline().rstrip('\r\n')

def read_ints():
    line = read_line()
    return map(int, line.split(' '))

def solve_radius(plant1, plant2):
    (x1, y1, r1) = plant1
    (x2, y2, r2) = plant2
    #print >> stderr, "watering", x1, y1, r2, x2, y2, r2
    ans = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2) + r1 + r2)/2
    #print >> stderr, ans
    return ans

def solve_case(plants):
    if len(plants) == 1:
        return plants[0][2]
    if len(plants) == 2:
        return max(plants[0][2], plants[1][2])
    # 3 plants
    options = [0, 0, 0]
    options[0] = max(solve_radius(plants[0], plants[1]), plants[2][2])
    options[1] = max(solve_radius(plants[0], plants[2]), plants[1][2])
    options[2] = max(solve_radius(plants[1], plants[2]), plants[0][2])
    return min(options)

if __name__ == '__main__':
    no_cases = read_ints()[0]
    print >> stderr, "No of cases", no_cases
    for case in xrange(no_cases):
        no_plants = read_ints()[0]
        plants = [0] * no_plants
        for plant_ix in xrange(no_plants):
            (x, y, r) = read_ints()
            plants[plant_ix] = (x, y, r)
        print >> stderr, "Solving case", (case+1)
        sol = solve_case(plants)
        print "Case #%d: %f" % (case+1, sol)
        
