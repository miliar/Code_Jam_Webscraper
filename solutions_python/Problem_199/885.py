import sys

def booleanize(tower):
    result = list()
    for char in tower:
        result.append(char=="+")
    return result

#print booleanize("++--+")

def strip_plusses(boolean_tower):
    while len(boolean_tower)> 0 and boolean_tower[0]:
        boolean_tower = boolean_tower[1:]
    return boolean_tower

def flip_head(tower, size):
    for index in range(size):
        tower[index] = not tower[index]
    return tower

def solve_tower(tower, size):
    flips = 0
    #print tower
    tower = strip_plusses(tower)
    while len(tower) >= size:
        tower = flip_head(tower, size)
        flips += 1
        tower = strip_plusses(tower)
        #print tower
    if len(tower) is 0:
        return str(flips)
    return "IMPOSSIBLE"


#print solve_tower(booleanize("+++---"), 2)



if __name__ == "__main__" and len(sys.argv) is 2:
    filename = sys.argv[1]
    infile = open(filename+".in", "r")
    outfile = open(filename+".out", "w")
    T = int(infile.readline())
    #print T
    for case in range(T):
        tower, size = infile.readline().split()
        print tower, size
        tower = booleanize(tower)
        size = int(size)
        result = solve_tower(tower, size)
        print result
        outfile.write("Case #{}: {}\n".format(case+1, result))
    infile.close()
    outfile.close()
