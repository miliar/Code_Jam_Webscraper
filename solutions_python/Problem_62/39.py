import copy
import sys
from pprint import pprint
from copy import deepcopy

input = file(sys.argv[1])
count = int(input.readline())
testcase = 1

if __name__ == '__main__':
    try:
        while testcase <= count:
            wires = int(input.readline())
            left_building = [0 for x in range(10**4 + 1)]
            for wire in range(wires):
                a, b = map(int, input.readline().split())
                left_building[a] = b
            intersections = 0
            uncount_wires = wires
            for floor in range(len(left_building)):
                left = left_building.pop(0)
                if left == 0:
                    continue
                uncount_wires -= 1
                if not uncount_wires:
                    break
                for other_left in left_building:
                    if other_left:
                        if other_left < left:
                            intersections += 1
            result = str(intersections)
            print 'Case #%i: %s' % (testcase, result)
            testcase += 1
    except:
        import pdb;pdb.post_mortem()
