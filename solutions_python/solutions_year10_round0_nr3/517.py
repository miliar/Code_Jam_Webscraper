import sys

RUNS = 0
CAPACITY = 1
GROUPS = 2

def do_case(case):
    euros = 0
    groups = case[GROUPS]
    
    for i in xrange(case[RUNS]):
        capacity = case[CAPACITY]
        groups_on_coaster = []
        
        while len(groups) > 0 and capacity >= groups[0]:
            euros += groups[0]
            capacity -= groups[0]
            groups_on_coaster.append(groups.pop(0))
        
        groups += groups_on_coaster
    
    return euros

if __name__ == "__main__":
    lines = open(sys.argv[1], "r").readlines()
    
    for i in xrange(1, len(lines), 2):
        line1 = [int(num) for num in lines[i].split()]
        line2 = [int(num) for num in lines[i + 1].split()]
        print("Case #%d: %d" % ((i // 2) + 1, do_case((line1[0], line1[1], line2))))
