import sys

def read_line():
    return sys.stdin.readline().strip()
    
T = int(read_line())

def process_testcase():
    answer1 = int(read_line())
    grid1 = []
    for i in range(0, 4):
        grid1.append(read_line().split(' '))
    answer2 = int(read_line())
    grid2 = []
    for i in range(0, 4):
        grid2.append(read_line().split(' '))    
    
    intersection = set(grid1[answer1-1]) & set(grid2[answer2-1])
    if len(intersection) == 0:
        return "Volunteer cheated!"
    elif len(intersection) == 1:
        return list(intersection)[0]
    else:
        return "Bad magician!"

for i in range(0, T):
    r = process_testcase()
    print "Case #%d: %s" % (i+1, r)
